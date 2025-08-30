# SPARC Methodology: Agent Implementation Guide

## Overview for AI Agents

This document provides AI agents with comprehensive instructions for implementing the SPARC methodology to create detailed phase-specific documentation. Use this guide to understand how to break down any development project into the five SPARC phases and generate appropriate markdown files for each.

## What is SPARC?

SPARC (Specification, Pseudocode, Architecture, Refinement, Completion) is a structured methodology that transforms software development from ad-hoc coding into a disciplined, systematic approach. Each phase builds upon the previous one, ensuring comprehensive coverage and maintainability.

**Core Flow**: S → P → A → R → C (Specification → Pseudocode → Architecture → Refinement → Completion)

## Key Principles for Agents

1. **Sequential Development**: Each phase must be completed before moving to the next
2. **Comprehensive Documentation**: Every phase requires detailed markdown documentation
3. **Reflective Analysis**: Include justifications for all decisions and consider alternatives
4. **Test-Driven Approach**: Define testing criteria from the specification phase
5. **Iterative Refinement**: Each phase may require revisiting previous phases
6. **Stakeholder Communication**: Write documentation that technical and non-technical stakeholders can understand

## The Five SPARC Phases - Agent Instructions

### Phase 1: Specification (S)
**Your Role**: Requirements Analyst & Domain Expert

**Objective**: Create a comprehensive specification document that serves as the project's foundation.

**What You Must Produce**:
- Detailed project specification markdown file
- Clear functional and non-functional requirements
- User scenarios and acceptance criteria
- Technical constraints and assumptions

**Agent Template for Specification Phase**:
```markdown
# [Project Name] - Specification Phase

## Project Overview
- **Project Goal**: [Clear statement of what the project aims to achieve]
- **Target Audience**: [Detailed description of intended users]
- **Project Scope**: [What is included and explicitly what is not]

## Functional Requirements
[List each feature with detailed descriptions, broken into manageable components]

## Non-Functional Requirements
- **Performance**: [Response times, throughput, scalability targets]
- **Security**: [Authentication, authorization, data protection]
- **Usability**: [User experience standards, accessibility]
- **Reliability**: [Uptime, error handling, backup requirements]

## User Scenarios
[Detailed user flow descriptions with step-by-step interactions]

## UI/UX Guidelines
[Design principles, style guidelines, user experience standards]

## Technical Constraints
[Technology preferences, limitations, integration requirements]

## Assumptions
[All assumptions made during specification with justifications]

## Success Criteria
[Measurable criteria for project success]

## Reflection
[Justify decisions made, consider alternatives, discuss potential challenges]
```

### Phase 2: Pseudocode (P)
**Your Role**: Algorithm Designer & Logic Architect

**Objective**: Transform specifications into high-level algorithmic design that serves as an implementation roadmap.

**What You Must Produce**:
- Detailed pseudocode for all major functions
- Algorithm design with complexity analysis
- Data structure definitions
- Logic flow diagrams in text format

**Agent Template for Pseudocode Phase**:
```markdown
# [Project Name] - Pseudocode Phase

## High-Level System Flow
[Overall application logic and data flow]

## Core Algorithms
### [Algorithm Name]
```
ALGORITHM: [Name]
INPUT: [Parameters with types]
OUTPUT: [Return values with types]

BEGIN
    [Step-by-step pseudocode]
    // Comments explaining complex logic
    IF condition THEN
        [conditional logic]
    END IF
    
    FOR each item IN collection DO
        [iteration logic]
    END FOR
    
    RETURN [result]
END
```

## Data Structures
[Define all data models, schemas, and structures]

## Function Definitions
[High-level function signatures and purposes]

## Error Handling Strategy
[How errors will be detected, handled, and reported]

## Performance Considerations
[Algorithm complexity analysis, optimization opportunities]

## Reflection
[Justify algorithmic choices, consider alternatives, identify potential issues]
```

### Phase 3: Architecture (A)
**Your Role**: System Architect & Technical Designer

**Objective**: Define the system architecture, component interactions, and technical design.

**What You Must Produce**:
- System architecture documentation
- Component interaction diagrams
- Technology stack decisions
- Database design and data models
- API specifications

**Agent Template for Architecture Phase**:
```markdown
# [Project Name] - Architecture Phase

## System Architecture Overview
[High-level system design with component descriptions]

## Architectural Style
- **Pattern**: [MVC, Microservices, Layered, etc.]
- **Justification**: [Why this pattern was chosen]

## Technology Stack
### Frontend
- **Framework**: [Choice with justification]
- **Additional Libraries**: [List with purposes]

### Backend
- **Runtime/Framework**: [Choice with justification]
- **Additional Libraries**: [List with purposes]

### Database
- **Type**: [SQL/NoSQL with justification]
- **Specific Technology**: [PostgreSQL, MongoDB, etc.]

### Infrastructure
- **Hosting**: [Cloud provider, containerization]
- **CI/CD**: [Deployment strategy]

## System Components
### [Component Name]
- **Purpose**: [What this component does]
- **Responsibilities**: [Specific duties]
- **Interfaces**: [How other components interact with it]
- **Dependencies**: [What it depends on]

## Data Architecture
### Database Schema
[Tables, relationships, indexes]

### Data Flow
[How data moves through the system]

## API Design
### Endpoints
- **GET /api/[resource]**: [Purpose and response]
- **POST /api/[resource]**: [Purpose and payload]

## Security Architecture
[Authentication, authorization, data protection strategies]

## Scalability Considerations
[How the system will handle growth]

## Reflection
[Architectural decisions justification, alternatives considered, trade-offs]
```

### Phase 4: Refinement (R)
**Your Role**: Code Quality Engineer & Performance Optimizer

**Objective**: Iteratively improve the design and implementation through testing and optimization.

**What You Must Produce**:
- Test strategy and test cases
- Performance optimization plans
- Code quality guidelines
- Refactoring recommendations

**Agent Template for Refinement Phase**:
```markdown
# [Project Name] - Refinement Phase

## Testing Strategy
### Test Types
- **Unit Tests**: [Components to test, coverage targets]
- **Integration Tests**: [Component interaction tests]
- **End-to-End Tests**: [User scenario testing]
- **Performance Tests**: [Load testing, benchmarks]

### Test Cases
#### [Feature Name] Test Cases
```
Test: [Test name]
Given: [Initial conditions]
When: [Action taken]
Then: [Expected outcome]
```

## Performance Optimization
### Identified Bottlenecks
[Performance issues found in design/pseudocode]

### Optimization Strategies
[Specific improvements to implement]

## Code Quality Standards
### Coding Conventions
[Style guidelines, naming conventions]

### Documentation Requirements
[Code comments, API documentation standards]

## Refactoring Plan
### Areas for Improvement
[Components that need refactoring]

### Refactoring Strategies
[How to improve code structure]

## Review Checklist
- [ ] All functional requirements addressed
- [ ] Non-functional requirements met
- [ ] Test coverage adequate
- [ ] Performance targets achieved
- [ ] Security requirements implemented
- [ ] Documentation complete

## Reflection
[Analysis of design improvements, testing strategy justification]
```

### Phase 5: Completion (C)
**Your Role**: Deployment Engineer & Project Finalizer

**Objective**: Finalize the project for production deployment with comprehensive documentation and monitoring.

**What You Must Produce**:
- Deployment strategy and procedures
- Production readiness checklist
- User documentation
- Maintenance and monitoring plans

**Agent Template for Completion Phase**:
```markdown
# [Project Name] - Completion Phase

## Deployment Strategy
### Environment Configuration
- **Development**: [Setup and configuration]
- **Staging**: [Testing environment setup]
- **Production**: [Live environment configuration]

### Deployment Procedures
1. [Step-by-step deployment process]
2. [Verification procedures]
3. [Rollback procedures]

## Production Readiness Checklist
### Infrastructure
- [ ] Server provisioning complete
- [ ] Database setup and configured
- [ ] SSL certificates installed
- [ ] Load balancing configured
- [ ] Backup systems in place

### Application
- [ ] All tests passing
- [ ] Performance benchmarks met
- [ ] Security audit completed
- [ ] Error handling implemented
- [ ] Logging configured

### Documentation
- [ ] User documentation complete
- [ ] API documentation published
- [ ] Admin documentation ready
- [ ] Troubleshooting guides created

## User Documentation
### Getting Started Guide
[Step-by-step user onboarding]

### Feature Documentation
[Detailed feature explanations with examples]

### FAQ
[Common questions and answers]

## Monitoring and Maintenance
### Monitoring Setup
- **Application Monitoring**: [Tools and metrics]
- **Infrastructure Monitoring**: [Server health, database performance]
- **User Analytics**: [Usage tracking, performance metrics]

### Maintenance Procedures
- **Regular Updates**: [Update schedule and procedures]
- **Backup Procedures**: [Data backup and recovery]
- **Performance Optimization**: [Ongoing improvement processes]

## Post-Launch Support
### Issue Tracking
[Bug reporting and resolution procedures]

### Feature Requests
[Process for handling new feature requests]

## Project Summary
### Goals Achieved
[Verification that all original objectives were met]

### Lessons Learned
[Key insights from the development process]

### Future Enhancements
[Potential improvements and additions]

## Reflection
[Overall project assessment, process effectiveness, recommendations for future projects]
```

## How to Use This Guide as an Agent

### Step 1: Project Analysis and User Consultation
When given a project, first analyze what type of system is being requested, then **actively engage with the user** to gather comprehensive information:

**Required User Consultation Steps:**
1. **Clarify Project Vision**: Ask the user to elaborate on unclear aspects of the project description
2. **Gather Missing Requirements**: Identify and request information about functional and non-functional requirements
3. **Understand Constraints**: Ask about technical limitations, timeline constraints, and resource availability
4. **Validate Assumptions**: Present your understanding of the project and ask the user to confirm or correct it
5. **Identify Stakeholders**: Ask who the end users are and who will be involved in the project
6. **Define Success Criteria**: Work with the user to establish measurable success metrics

**Key Questions to Ask Users:**
- "Can you provide more details about [specific unclear aspect]?"
- "What are the primary goals you want to achieve with this project?"
- "Who are your target users and what problems are you solving for them?"
- "Are there any technical constraints or preferences I should be aware of?"
- "What does success look like for this project?"
- "What timeline are you working with?"

### Step 2: Phase Selection
Determine which SPARC phase is most appropriate to start with (usually Specification, but sometimes you might be asked to focus on a specific phase).

### Step 3: Template Application
Use the appropriate phase template and customize it for the specific project requirements.

### Step 4: Documentation Generation
Create comprehensive markdown documentation following the template structure, ensuring all sections are thoroughly completed.

### Step 5: Reflection Integration
Always include the reflection section with thoughtful analysis of decisions made and alternatives considered.

## Agent Prompt Templates

### General SPARC Implementation Prompt
```
I need you to act as a SPARC methodology expert and create a [PHASE] document for [PROJECT_DESCRIPTION]. 

**IMPORTANT: Before proceeding with documentation, you MUST first ask the user clarifying questions to gather complete information.**

Follow this process:
1. **ASK THE USER**: Review the project description and ask specific questions to clarify any unclear aspects, missing requirements, constraints, or assumptions
2. **WAIT FOR RESPONSES**: Do not proceed until the user has provided the requested information
3. **VALIDATE UNDERSTANDING**: Summarize your understanding and ask the user to confirm it's correct

Then follow the SPARC [PHASE] template exactly, ensuring you:
1. Research the domain thoroughly if needed
2. Fill out all required sections comprehensively based on user input
3. Include detailed explanations and justifications
4. Consider alternatives and trade-offs
5. Provide actionable, specific information
6. Include a thorough reflection section

Output should be a complete markdown document ready for implementation use.
```

### Phase-Specific Prompts
```
**Specification Phase**: "Create a comprehensive SPARC Specification document for [PROJECT]. FIRST, ask the user detailed questions about requirements, constraints, target users, success criteria, and any unclear aspects of the project. Wait for their responses before proceeding. Then include all functional/non-functional requirements, user scenarios, technical constraints, and assumptions. Ensure the specification is detailed enough that any developer could understand the project requirements."

**Pseudocode Phase**: "Develop detailed SPARC Pseudocode documentation for [PROJECT] based on the specification. FIRST, ask the user about any algorithmic preferences, performance requirements, or implementation constraints they have. Wait for their responses. Then include high-level algorithms, data structures, function definitions, and logic flow. Focus on algorithmic thinking before implementation."

**Architecture Phase**: "Design a complete SPARC Architecture document for [PROJECT]. FIRST, ask the user about technology preferences, infrastructure constraints, scalability requirements, and integration needs. Wait for their responses. Then include system components, technology stack decisions, database design, API specifications, and security considerations. Justify all architectural choices."

**Refinement Phase**: "Create a SPARC Refinement plan for [PROJECT]. FIRST, ask the user about testing preferences, quality standards, performance targets, and any specific concerns they have. Wait for their responses. Then include comprehensive testing strategy, performance optimization plans, code quality standards, and refactoring recommendations. Focus on improving quality and maintainability."

**Completion Phase**: "Develop a SPARC Completion document for [PROJECT]. FIRST, ask the user about deployment preferences, documentation requirements, maintenance expectations, and support processes. Wait for their responses. Then include deployment strategy, production readiness checklist, user documentation, and maintenance procedures. Ensure the project is ready for production launch."
```

## Best Practices for Agents

1. **Always Consult Users First**: Before creating any documentation, ask clarifying questions and gather missing information from users
2. **Be Comprehensive**: Don't skip sections; every part of the template serves a purpose
3. **Think Critically**: Always question assumptions and consider alternatives
4. **Stay Practical**: Provide actionable information, not just theoretical concepts
5. **Maintain Consistency**: Ensure each phase builds logically on the previous ones
6. **Focus on Quality**: Better to have thorough documentation than rushed completion
7. **Consider Stakeholders**: Write for both technical and non-technical audiences
8. **Plan for Change**: Build flexibility into your documentation for future modifications
9. **Validate Understanding**: Regularly confirm with users that your interpretation is correct
10. **Ask Follow-up Questions**: Don't hesitate to ask for more details when something is unclear

This guide enables any AI agent to effectively implement the SPARC methodology and create comprehensive project documentation that follows proven software development practices.