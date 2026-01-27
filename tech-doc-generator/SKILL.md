---
name: tech-doc-generator
description: Generate comprehensive technical development documentation for science and technology innovation projects. Use when users request help writing project documentation, technical reports, or academic papers for student competitions (like science fairs, innovation contests). Supports hardware projects, software projects, and integrated systems. Adapts documentation complexity to student grade level (elementary, middle school, high school).
---

# Technical Development Documentation Generator

## Overview

Generate complete, professional technical documentation for student science and technology innovation projects. Transform simple project descriptions into comprehensive documents suitable for competitions, academic evaluation, and project presentations.

## Workflow

### Step 1: Gather Project Information

Ask targeted questions to understand the project. ALWAYS start with these essential questions:

**Basic Information:**
- Project name and brief description
- Student grade level (elementary/middle/high school)
- Project type: hardware, software, or integrated system
- Competition/purpose (science fair, innovation contest, academic paper, etc.)

**Project Details:**
- What problem does it solve?
- How does it work? (brief technical overview)
- What materials/technologies are used?
- Current development status (concept, prototype, completed)

**Existing Materials:**
- Any code, schematics, or design files
- Photos or diagrams
- Test data or results
- Previous documentation attempts

### Step 2: Determine Documentation Scope

Based on gathered information, propose a documentation structure. Refer to `references/document-structures.md` for templates matching:
- Grade level (elementary, middle, high school)
- Project type (hardware, software, system)
- Competition requirements

Confirm with user which sections to include.

### Step 3: Generate Documentation Sections

Create sections progressively, allowing user review between sections. Default order:

**For Competition Papers:**
1. Cover page & abstract
2. Project background & motivation
3. Research objectives & significance
4. Technical approach & system design
5. Implementation details
6. Testing & results
7. Innovation points & contributions
8. Conclusions & future work
9. References & acknowledgments

**For Technical Reports:**
1. Executive summary
2. System architecture
3. Hardware/software design details
4. Development process
5. User manual
6. Troubleshooting guide

### Step 4: Adapt Content to Grade Level

**Elementary School:**
- Simple language, story-like narrative
- Focus on observation and hands-on experience
- Include drawings, photos, step-by-step photos
- Emphasize "what I learned" and "what I tried"

**Middle School:**
- Introduce basic technical terms with explanations
- Show understanding of scientific method
- Include simple data tables and graphs
- Explain cause-and-effect relationships

**High School:**
- Technical terminology with proper definitions
- Detailed methodology and analysis
- Statistical data, charts, formulas
- Literature review and citations
- Discussion of limitations and improvements

### Step 5: Format and Finalize

Create the document in appropriate format:
- Use `create_file` for markdown drafts
- Convert to Word (.docx) if requested using docx skill
- Include proper formatting: headers, numbering, citations
- Add table of contents for documents >10 pages
- Place final document in `/mnt/user-data/outputs/`

## Content Generation Guidelines

### Technical Accuracy
- Verify technical details don't contradict each other
- Ensure code examples are syntactically correct
- Check units and measurements are consistent
- Validate that claimed innovations are novel

### Project Type Specialization

**Hardware Projects:**
- Emphasize component selection rationale
- Include circuit diagrams, wiring diagrams
- Explain mechanical design considerations
- Document assembly process with photos
- Provide troubleshooting for common issues

**Software Projects:**
- Show system architecture diagrams
- Include key code snippets with explanations
- Explain algorithm choices
- Document API/interface design
- Include user interface screenshots

**Integrated Systems:**
- Clearly separate hardware and software components
- Explain communication protocols between components
- Show system integration architecture
- Discuss hardware-software co-design decisions

### Common Sections

**Problem Statement:**
- Start with real-world observation or personal experience
- Use specific examples and data
- Explain why existing solutions are insufficient
- State clear, measurable objectives

**Innovation Points:**
- Highlight what makes this project unique
- Compare with existing solutions
- Quantify improvements (faster, cheaper, more accurate)
- Explain technical innovations clearly

**Testing & Results:**
- Design meaningful test cases
- Present data in tables and graphs
- Include both successful and unsuccessful attempts
- Discuss what was learned from failures

**Future Improvements:**
- Acknowledge current limitations honestly
- Propose realistic next steps
- Consider cost, complexity, and feasibility

## Document Quality Standards

### Writing Style
- Clear, concise sentences (vary length for readability)
- Active voice preferred over passive
- Define technical terms on first use
- Use consistent terminology throughout

### Visual Elements
- Every diagram/photo should have a caption
- Label all axes on graphs
- Use consistent color schemes
- Ensure images are high resolution

### Citations
- Use consistent citation format (IEEE, APA, etc.)
- Cite sources for technical data, existing solutions
- Include both academic and web sources where appropriate
- Never invent citations

## Handling Edge Cases

**Incomplete Projects:**
- Document current progress honestly
- Include planned features in "Future Work"
- Explain technical challenges encountered
- Show problem-solving process

**Limited Technical Knowledge:**
- Ask follow-up questions to understand intent
- Suggest simplified explanations
- Offer to research specific technical details
- Recommend appropriate complexity level

**Translation Needs:**
- Primary language is Chinese (用户主要使用中文)
- Use Chinese for all documentation by default
- Provide English abstracts if requested
- Use standard technical terminology in English where appropriate

## Resources

### references/document-structures.md
Templates and structural guidance for different types of projects and grade levels.

### references/examples.md
Real examples from previously created documentation to illustrate best practices.

### references/chinese-templates.md
Chinese language templates and common phrases for technical documentation.
