---
name: firmware-build-verify
description: >
  Firmware build, upload, and serial verification workflow. MUST be triggered after writing or
  modifying any Arduino/ESP32/embedded firmware code. Automatically detects the project type
  (Arduino CLI or PlatformIO), compiles the code, reports and fixes errors until compilation
  succeeds, uploads firmware to the connected board, and verifies runtime behavior via serial
  output. Code is NOT considered complete until compilation passes successfully.
---

# Firmware Build & Verify Workflow

You MUST run this workflow after writing or modifying any firmware code for Arduino, ESP32, STM32,
or any microcontroller project. **Code is NOT considered done until it compiles successfully.**

## Environment

The following tools are available on this machine:

- **arduino-cli** (`/opt/homebrew/bin/arduino-cli`) — Arduino CLI v1.2.2
- **platformio** (`/Users/zunwei/Library/Python/3.9/bin/pio`) — PlatformIO Core v6.1.19
- **serial-mcp** — MCP server for serial port communication (if configured)

### Installed Arduino Cores
- `arduino:avr` — Arduino AVR Boards (Uno, Mega, Nano, etc.)
- `arduino:esp32` — Arduino ESP32 Boards
- `esp32:esp32` — Espressif ESP32 Boards (v3.3.5)

### Default Board Mappings

| Board | Arduino CLI FQBN | PlatformIO board | PlatformIO framework |
|-------|-----------------|------------------|---------------------|
| ESP32 DevKit | `esp32:esp32:esp32` | `esp32dev` | `arduino` or `espidf` |
| ESP32-S3 | `esp32:esp32:esp32s3` | `esp32-s3-devkitc-1` | `arduino` or `espidf` |
| Arduino Uno | `arduino:avr:uno` | `uno` | `arduino` |
| Arduino Mega | `arduino:avr:mega` | `megaatmega2560` | `arduino` |

## Step 1: Detect Project Type

Before compiling, determine which build system the project uses:

**PlatformIO project** — if any of these exist:
- `platformio.ini` in the project root
- `.pio/` directory
- `src/main.cpp`

**Arduino CLI project** — if any of these exist:
- `.ino` file in the project directory
- No `platformio.ini` present

**If both exist**, prefer PlatformIO (more complete dependency management).

## Step 2: Compile

### PlatformIO Compile
```bash
# Basic compile (all environments in platformio.ini)
cd <project_root> && pio run

# Compile specific environment
cd <project_root> && pio run -e esp32dev

# Verbose output for debugging compile issues
cd <project_root> && pio run -v
```

### Arduino CLI Compile
```bash
# Determine the FQBN based on the target board
# ESP32 DevKit:
arduino-cli compile --fqbn esp32:esp32:esp32 <sketch_path>

# ESP32-S3:
arduino-cli compile --fqbn esp32:esp32:esp32s3 <sketch_path>

# Arduino Uno:
arduino-cli compile --fqbn arduino:avr:uno <sketch_path>

# Arduino Mega:
arduino-cli compile --fqbn arduino:avr:mega:cpu=atmega2560 <sketch_path>

# Show memory usage
arduino-cli compile --fqbn <fqbn> --show-properties <sketch_path>
```

### Compile Error Handling

When compilation fails, follow this process:

1. **Read the FULL error output** — don't just look at the first error
2. **Identify the root cause** — often the first error causes cascading errors
3. **Common error categories:**
   - **Missing library** → `pio lib install <lib>` or `arduino-cli lib install <lib>`
   - **Type mismatch** → Check variable types, especially `int` vs `uint32_t` on different platforms
   - **Missing include** → Add the correct `#include` header
   - **Platform-specific API** → e.g., `analogReadResolution()` exists on ESP32 but not AVR
   - **Pin conflict** → Check pin assignments against the board's pinout
4. **Fix the code and recompile** — repeat until zero errors and zero warnings
5. **Check memory usage** — ensure RAM and Flash usage are within limits:
   - AVR (Uno): 2KB RAM, 32KB Flash — watch carefully
   - ESP32: 320KB RAM, 4MB Flash — more forgiving but watch PSRAM allocation

### Compile Success Criteria
- Zero errors
- Zero warnings (or only known/acceptable warnings from library code)
- Flash usage < 90% of available space
- RAM usage < 80% of available space (leave room for runtime allocations)

## Step 3: Upload (when board is connected)

Before uploading, detect the connected board:

```bash
# List connected boards
arduino-cli board list

# PlatformIO auto-detect
pio device list
```

### Upload Commands

```bash
# PlatformIO upload (auto-detects port)
cd <project_root> && pio run -t upload

# PlatformIO upload to specific port
cd <project_root> && pio run -t upload --upload-port /dev/cu.usbserial-XXXX

# Arduino CLI upload
arduino-cli upload --fqbn <fqbn> --port /dev/cu.usbserial-XXXX <sketch_path>
```

### Upload Troubleshooting
- **"No such file or directory"** → Board not connected or wrong port
- **"Permission denied"** → Run `sudo chmod 666 /dev/cu.usbserial-XXXX`
- **"Failed to connect to ESP32"** → Hold BOOT button during upload
- **"A fatal error occurred: Could not open port"** → Close any serial monitor first
- **ESP32-S3 USB** → May appear as `/dev/cu.usbmodem*` instead of `/dev/cu.usbserial*`

## Step 4: Serial Verification (after upload)

After successful upload, verify the firmware is running correctly:

### Using serial-mcp (if available as MCP tool)
```
1. Call arduino_serial_open with the port and baud rate (usually 115200)
2. Wait 2-3 seconds for boot messages
3. Call arduino_serial_read to check output
4. Look for:
   - Normal boot sequence (no crash/reboot loop)
   - Expected sensor readings or status messages
   - No Guru Meditation Errors
   - No stack overflow warnings
   - No watchdog timeout messages
5. Call arduino_serial_close when done
```

### Using PlatformIO serial monitor
```bash
# Open serial monitor
pio device monitor -b 115200

# With specific port
pio device monitor -p /dev/cu.usbserial-XXXX -b 115200
```

### Using Arduino CLI serial monitor
```bash
arduino-cli monitor -p /dev/cu.usbserial-XXXX --config baudrate=115200
```

### What to Check in Serial Output
- **Boot messages** — Should show normal initialization, not crash loops
- **Sensor data** — Values should be in expected ranges (not 0, NaN, or -1)
- **WiFi connection** — Should show "Connected" with IP address if applicable
- **Memory** — Free heap should be stable, not decreasing over time
- **Error messages** — Any "E (" prefixed messages from ESP-IDF indicate errors

## Workflow Summary

```
Write/Edit Code
      │
      ▼
┌─────────────┐
│  Compile     │◄──── Fix errors ◄─┐
└──────┬──────┘                    │
       │ Pass?                     │
       │ No ───────────────────────┘
       │ Yes
       ▼
┌─────────────┐
│  Upload      │ (only if board connected)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Serial      │ (verify runtime behavior)
│  Monitor     │
└──────┬──────┘
       │
       ▼
   ✅ DONE — Code is verified
```

## Important Rules

1. **NEVER tell the user "code is complete" if compilation has not been attempted**
2. **ALWAYS compile after any code modification** — even small changes can break things
3. **If the user hasn't specified a board**, ask which board they're targeting
4. **If compilation fails, fix and retry** — do not give up after one attempt
5. **Report memory usage** after successful compilation — especially important for AVR boards
6. **If upload fails due to no board connected**, that's OK — compilation success is the minimum bar
7. **Cross-platform awareness**: Code that compiles for ESP32 may not compile for AVR and vice versa. If the user targets multiple boards, compile for all of them.
