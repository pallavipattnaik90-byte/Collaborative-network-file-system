Computer Networks Mini Project
Assignment 2 — Collaborative Network File System

1. Project Information
Course: Computer Networks
Assignment: Assignment 2 — Mini Project
Selected Project: Project 4 — Collaborative Network File System
Team Size: 3 Members
Final Submission Deadline: 11 October 2026
Initial Project Write-up Deadline: Sunday, 20 September 2026
Team Members
Member	Name	Roll No.
Member 1	ASHISH ROY	24155761
Member 2	PALLAVI PATTNAIK	24155785
Member 3	AMRIT RAJ	24155679

2. Project Choice
We have selected Project 4: Collaborative Network File System from the four mini-project options provided for the Computer Networks course.
The project involves building a server-backed file system in which multiple clients can connect to the same server, access a shared file, make changes, and receive updates from the server.
The project is based on a client-server architecture. A central server will maintain the shared file and coordinate communication between multiple clients.
The system will support at least three simultaneous clients, allowing them to edit the shared file and observe changes propagated through the server.
According to the project specification, the system must also have a clearly defined method for dealing with concurrent/conflicting edits, handle client disconnection and re-connection, and demonstrate a deliberate conflict scenario during the final live demonstration.

3. Why We Chose This Project
We selected the Collaborative Network File System because it provides a practical way to demonstrate important Computer Networks concepts without requiring multiple physical computers or complicated hardware.
Our previous attempts to establish communication between multiple devices using the Ubuntu application on Windows were unsuccessful. We also faced difficulties with sharing files between hosts.
Therefore, for this project, we plan to use a single host machine and run the server and multiple clients locally.
The proposed setup will use:
                 Same Host / Ubuntu Environment

                    ┌──────────────┐
                         │    SERVER    │
                          │   localhost │
                    └──────┬───────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        ┌─────────┐   ┌─────────┐   ┌─────────┐
           │ Client 1│         │ Client 2│         │ Client 3│
        └─────────┘   └─────────┘   └─────────┘
All three clients will communicate with the server through the local network interface.
This approach allows us to demonstrate networking concepts such as:

Client-server communication


Socket communication


Multiple simultaneous connections


Data transfer


Synchronization


Concurrent access


Conflict handling


Client disconnection and reconnection

without depending on three separate physical devices.

4. Proposed Project Objective
The primary objective of this project is to develop a small-scale collaborative file system where:
1.A server maintains a shared file.
2.Multiple clients can connect to the server.
3.At least three clients can remain connected simultaneously.
4.Clients can view the shared file.
5.Clients can make edits to the shared file.
6.Changes made by a client are sent to the server.
7.The server maintains the authoritative version of the file.
8.The server propagates changes to other connected clients.
9.Simultaneous/conflicting edits are handled according to a predefined strategy.
10.A disconnected client can reconnect and obtain a consistent version of the file.
These objectives directly correspond to the core requirements specified for Project 4.

5. Proposed System Architecture
The project will follow a centralized client-server architecture.
Server
The server will act as the central source of truth for the shared file.
Its responsibilities will include:
Accepting client connections.
Maintaining a list of connected clients.
Maintaining the current version of the shared file.
Receiving edit requests from clients.
Processing edits.
Handling conflicting edits.
Updating the shared file.
Sending updated content to connected clients.
Handling client disconnections.
Sending the latest file state to clients when they reconnect.
Clients
Each client will:
Connect to the server.
Request the current shared file.
Display the file.
Allow the user to make an edit.
Send the edit to the server.
Receive updated content from the server.
Update its local view.
Reconnect if the connection is lost.

6. Proposed Communication Flow
A simplified communication flow will be:
Client 1 ────────┐
                 │
Client 2 ────────┼──────> Server
                 │                   │
Client 3 ────────┘              │
                                      │
                                 Shared File
                                      │
                                      ▼
                             Updated File State
                                       │
               ┌─────────────┼─────────────┐
               ▼                      ▼                     ▼
            Client 1                Client 2             Client 3
For example:
1.Three clients connect to the server.
2.The server sends the current shared file to all clients.
3.Client 1 edits the file.
4.Client 1 sends the change to the server.
5.The server validates and applies the change.
6.The server updates the shared file.
7.The server sends the updated state to the other clients.
8.All clients eventually display the same consistent state.

7. Conflict Resolution Strategy
One of the most important requirements of this project is that concurrent edits cannot be handled randomly.
The project specification specifically requires a clear and deliberate strategy for concurrent conflicting edits and requires the team to explain why that strategy was selected.
For our initial design, we plan to use a server-controlled version/locking approach rather than attempting a highly complex collaborative editing algorithm.
The server will remain the authoritative source of the file.
A simplified approach will be:
Client requests edit
        ↓
Server checks current file/version
        ↓
Is the edit based on the current version?
       / \
     YES  NO
      |    |
      ▼    ▼
   Accept  Conflict
      |    |
      ▼    ▼
 Update   Reject/request refresh
 server   latest version
This makes the behavior predictable and easier to demonstrate.
The exact implementation details of the conflict mechanism will be finalized during development and documented in the final design document.

8. Example Conflict Scenario
The live demonstration will include a deliberate conflict.
For example:
Initial file:

Hello World
Computer Networks
Mini Project
Suppose Client 1 and Client 2 both receive the same version of the file.
Client 1 attempts to change:
Hello World
to:
Hello KIIT
At approximately the same time, Client 2 attempts to change the same original content to:
Hello Students
The server will detect that the two operations are based on the same/older version and apply the predefined conflict-resolution mechanism.
The important point is that the result should be predictable and explainable, rather than depending on undefined behavior.
The project specification explicitly requires a realistic conflicting-edit demonstration.

9. Three-Client Requirement
The final system will support at least three simultaneous clients:
                 SERVER
                   │
       ┌───────────┼───────────┐
       │           │           │
       ▼           ▼           ▼
   CLIENT 1    CLIENT 2    CLIENT 3
Since our system will initially be tested on one host, these can be separate client processes running simultaneously.
For example:
Terminal 1 → Server
Terminal 2 → Client 1
Terminal 3 → Client 2
Terminal 4 → Client 3
This will allow us to demonstrate multiple network endpoints without requiring three physical machines.

10. Same-Host Implementation Plan
Because our previous attempts to connect multiple devices using the Ubuntu application on Windows were unsuccessful, the project will initially be designed to operate completely on one host.
The expected setup will be:
Windows
   │
   └── Ubuntu / WSL
          │
          ├── Server
          │
          ├── Client 1
          │
          ├── Client 2
          │
          └── Client 3
The communication can use the local host interface, such as:
localhost
127.0.0.1
This means the project does not depend on transferring the shared file between different physical machines.
The shared file will remain under the control of the server.

11. Main Features Planned
The final project is planned to include the following features.
Essential Features
Server startup and shutdown.
Multiple client connections.
At least three simultaneous clients.
Shared file maintained by the server.
Client file viewing.
Client editing.
Sending edits to server.
Server-side synchronization.
Updated content propagation.
Conflict detection/handling.
Client disconnection handling.
Client reconnection.
Consistent file state.
Demonstration Features
The final demonstration will aim to show:
1.Server starting.
2.Three clients connecting.
3.Shared file being displayed.
4.Client 1 making an edit.
5.Other clients receiving the update.
6.Multiple clients editing.
7.A deliberate conflicting edit.
8.The conflict-resolution mechanism working.
9.One client disconnecting.
10.The client reconnecting.
11.The client receiving the latest consistent state.

12. AI Usage Declaration
AI tools will be used as a development and learning assistant during the project.
The team will not use AI as a substitute for understanding the project. All team members will study the implemented system and will be prepared to explain the architecture, networking concepts, code flow, conflict handling, and design decisions during the live evaluation.
Planned AI Usage
AI assistance may be used for:
Generating initial code structures.
Helping implement socket communication.
Assisting with client-server communication logic.
Assisting with multi-client/concurrent connection handling.
Helping implement file synchronization.
Helping implement the selected conflict-resolution mechanism.
Debugging programming errors.
Suggesting fixes for runtime errors.
Helping improve error handling.
Helping organize the project into separate files/modules.
Helping prepare documentation.
Helping interpret error messages.
Suggesting test cases.
Helping analyze basic performance or behavior observed during testing.
Important Restriction
AI-generated code will be reviewed, tested, modified, and understood by the team before being included in the final project.
The team will not knowingly include code that the members cannot explain during the final evaluation.

13. Parts We Will Personally Understand and Explain
Although AI may assist with implementation, the following areas will be specifically studied and understood by the three team members because these are relatively straightforward to explain during the live evaluation.
Member 1 — Networking and Server
Member 1 will primarily understand:
What a server is.
What a client is.
IP address and localhost.
Port number.
Socket.
TCP/client-server communication.
How the server accepts connections.
How multiple clients connect.
Basic server request-response flow.
Easy demonstration explanation:
"The server acts as the central point of communication. Clients connect to the server using sockets. Since we are running everything on the same machine, we use localhost. The server maintains the shared file and coordinates updates between clients."

Member 2 — Client and File Synchronization
Member 2 will primarily understand:
How a client connects to the server.
How the client requests the current file.
How an edit is sent to the server.
How the server sends an updated state back.
How multiple clients receive updates.
Basic file read/write operations.
Why the server should maintain the authoritative copy.
Easy demonstration explanation:
"The client does not independently decide the final state of the shared file. It sends its changes to the server. The server updates the authoritative file and then communicates the new state to the connected clients."

Member 3 — Concurrency and Conflict Handling
Member 3 will primarily understand:
Why simultaneous edits can cause conflicts.
What a concurrent edit means.
Why the server needs a conflict-resolution mechanism.
The selected version/locking strategy.
What happens when two clients edit at approximately the same time.
What happens when a client disconnects.
How a reconnecting client receives the current state.
Easy demonstration explanation:
"The problem occurs when two clients modify the same version of the file at nearly the same time. We therefore use a controlled strategy at the server so that conflicting operations are handled predictably instead of allowing the file to become inconsistent."

14. AI-Assisted Areas vs. Team-Owned Understanding
Area	AI Assistance	Team Understanding Required
Socket boilerplate	Yes	Basic socket concept
Server structure	Yes	How server accepts clients
Client structure	Yes	How client connects
File read/write code	Yes	Basic file operations
Multi-client handling	Yes	Why concurrency is required
Synchronization code	Yes	Basic synchronization flow
Conflict-resolution implementation	Yes	Full understanding of chosen strategy
Error handling	Yes	What errors are being handled
Reconnection logic	Yes	Why reconnection is necessary
Testing code	Yes	What each test demonstrates
Documentation	Yes	Team must verify contents
Debugging	Yes	Team must understand the final fix
Final architecture	AI may assist	Team must explain completely
Live demonstration	No replacement by AI	Entirely performed by team
The purpose of this division is not to avoid understanding the project. Rather, it allows the team to use AI for implementation assistance while focusing their preparation on the concepts and components that are most likely to be discussed during the live evaluation.

15. Division of Work
Member 1
Primary responsibility: Server and Networking
Tasks:
Server socket.
Port configuration.
Accepting client connections.
Maintaining connected-client information.
Basic communication protocol.
Server-side testing.

Member 2
Primary responsibility: Client and File Operations
Tasks:
Client socket.
Connecting to server.
Displaying shared file.
Sending edit requests.
Receiving updates.
File-related operations.
Client testing.

Member 3
Primary responsibility: Synchronization and Conflict Handling
Tasks:
Synchronization logic.
Conflict detection.
Conflict-resolution mechanism.
Disconnect/reconnect behavior.
Conflict test cases.
Multi-client testing.

Shared Responsibilities
All members will participate in:
Understanding the complete architecture.
Testing the final system.
Debugging.
Preparing the design document.
Preparing the live demonstration.
Reviewing the Git history.
Preparing for evaluation questions.
Each member should be capable of explaining the complete project at a basic level, even if a particular component is primarily assigned to another member.

16. Development Environment
The initial development environment is planned as:
Windows host machine.
Ubuntu environment/application on Windows.
Localhost networking.
Three client processes.
One server process.
Local shared file controlled by the server.
Git/GitHub for version control.
The exact programming language and supporting libraries will be finalized during implementation based on what allows the team to demonstrate the required networking concepts reliably.

17. Testing Plan
The system will be tested progressively rather than only at the end.
Test 1 — Server
Start the server and verify that it successfully listens for connections.
Test 2 — One Client
Connect one client and verify basic communication.
Test 3 — Multiple Clients
Connect three clients simultaneously.
Test 4 — File Retrieval
Verify that all clients can receive the current shared file.
Test 5 — Normal Edit
Modify the file from one client and verify that the update reaches the other clients.
Test 6 — Concurrent Editing
Have multiple clients make changes close together.
Test 7 — Conflict
Create a deliberate conflicting-edit scenario and verify that the predefined conflict strategy is followed.
Test 8 — Disconnect
Disconnect one client while the other clients continue operating.
Test 9 — Reconnect
Reconnect the disconnected client and verify that it receives a consistent current state.
Test 10 — Invalid/Unexpected Input
Test basic invalid requests or unexpected client behavior to make sure the server does not crash unnecessarily.

18. Live Demonstration Plan
The final demonstration will be performed live rather than through a prerecorded video.
This follows the project requirement that the system be demonstrated live.
Demonstration Sequence
STEP 1
Start Server
       ↓
STEP 2
Start Client 1
       ↓
STEP 3
Start Client 2
       ↓
STEP 4
Start Client 3
       ↓
STEP 5
Show common shared file
       ↓
STEP 6
Edit from Client 1
       ↓
STEP 7
Show update on other clients
       ↓
STEP 8
Create deliberate conflict
       ↓
STEP 9
Show conflict-resolution behavior
       ↓
STEP 10
Disconnect one client
       ↓
STEP 11
Continue using remaining clients
       ↓
STEP 12
Reconnect disconnected client
       ↓
STEP 13
Show consistent latest state
This sequence is intended to directly cover the major requirements of the project.

19. Git and Progressive Development
A major requirement of the assignment is that the Git commit history demonstrate that all group members worked on the assignment progressively throughout the allocated period.
The final submission therefore will not be based on a single last-minute commit.
The repository will contain meaningful commits throughout development.
Examples of appropriate commit stages include:
Initial project structure
Add basic server
Add basic client
Implement socket connection
Implement shared file handling
Add multiple client support
Add synchronization
Add conflict handling
Add disconnect handling
Add reconnect handling
Improve error handling
Testing and bug fixes
Documentation update
Final demonstration preparation
Final version
Each member will make meaningful contributions using their own Git account where possible.
The commit history will therefore provide evidence of progressive development and participation.

20. Proposed Repository Structure
The exact structure may change during development, but the initial plan is approximately:
collaborative-network-file-system/
│
├── README.md
│
├── server/
│   └── server code
│
├── client/
│   └── client code
│
├── shared/
│   └── shared file
│
├── tests/
│   └── testing files/scripts
│
├── docs/
│   └── design documentation
│
└── screenshots/
    └── demonstration screenshots
The final structure will depend on the implementation.

21. Expected Challenges
The following challenges are expected during development:
Multiple simultaneous connections
The server needs to communicate with multiple clients without one client unnecessarily blocking the others.
Synchronization
All clients need to eventually reflect the server's current state.
Concurrent edits
Two clients may attempt to modify the same data around the same time.
Conflict resolution
The system needs a predictable strategy for deciding how conflicting edits are handled.
Disconnection
A client may leave unexpectedly during operation.
Reconnection
A previously disconnected client needs to recover a consistent current state.
Live demonstration
The complete system needs to work reliably during the final evaluation.

22. Scope Control
To keep the project manageable, we will prioritize the requirements explicitly mentioned in the project specification.
We will not attempt to reproduce the full functionality of commercial collaborative editing systems such as Google Docs.
The project will instead demonstrate the core networking and distributed-system concepts required by the assignment:
Multiple clients.
Central server.
Shared mutable data.
Concurrent access.
Conflict handling.
Synchronization.
Disconnect/reconnect.
Consistency.
The project specification itself states that the conflict-resolution strategy does not need to be sophisticated, but it must be deliberate and explained.

23. Expected Final Deliverables
The final submission is expected to contain:
1. Working Client-Server System
A working implementation with source code and setup instructions.
2. Design Document
The document will explain:
System architecture.
Communication flow.
Client-server design.
Conflict-resolution strategy.
Reason for selecting the strategy.
Consistency behavior.
Limitations.
3. Live Demonstration
The demonstration will include:
At least three simultaneous clients.
Normal editing.
Synchronization.
A deliberate conflict scenario.
Defined conflict behavior.
Disconnect/reconnect demonstration.
4. Consistency Discussion
We will explain what consistency guarantees the system provides and what limitations remain.
These deliverables correspond to the official Project 4 requirements.

24. Project Timeline
Phase 1 — Project Selection and Planning
By 20 September 2026
Finalize team.
Finalize Project 4.
Submit project write-up.
Declare planned AI usage.
Decide initial architecture.
Decide development environment.
Phase 2 — Basic Networking
Implement server.
Implement client.
Establish basic socket communication.
Test localhost communication.
Phase 3 — Multiple Clients
Add multiple simultaneous clients.
Test three clients.
Handle client connections/disconnections.
Phase 4 — Shared File
Implement server-side shared file.
Implement reading and updating.
Synchronize clients.
Phase 5 — Conflict Handling
Implement selected conflict-resolution mechanism.
Test simultaneous edits.
Test deliberate conflicts.
Phase 6 — Reliability
Handle disconnects.
Implement reconnection.
Test invalid/unexpected situations.
Phase 7 — Testing and Documentation
Perform complete tests.
Fix bugs.
Prepare design document.
Update README.
Review Git history.
Phase 8 — Final Demonstration Preparation
Perform complete live demo.
Practice explaining architecture.
Practice explaining conflict handling.
Practice answering networking questions.
Verify all three members can explain their responsibilities
Final Deadline
11 October 2026
The final project, documentation, code, and required Git history will be prepared for submission by this deadline.

25. Evaluation Preparation
Since the project will be evaluated through a live demonstration and questioning, all members will prepare for questions such as:
Basic Networking
What is a socket?
What is localhost?
Why are we using a port?
What is the role of the server?
What is the role of a client?
How do multiple clients connect?
Project Architecture
Why did you use a client-server architecture?
Where is the authoritative copy of the file?
How are updates propagated?
What happens when a client disconnects?
Concurrency
What happens if two clients edit simultaneously?
Why can concurrent edits cause problems?
How does your system detect/handle a conflict?
Why did you choose this conflict-resolution method?
Consistency
Do all clients always have exactly the same state?
What happens during a temporary network failure?
What happens when a client reconnects?
Implementation
Which component handles connections?
How does the server communicate with clients?
How is the shared file updated?
How does the client receive the latest state?
Each team member will be prepared to explain both their assigned component and the overall project flow.

26. Final Project Goal
The goal is to create a small but reliable collaborative network file system that clearly demonstrates Computer Networks concepts rather than attempting to build a commercially complete collaborative editing platform.
The final system should allow three clients to communicate with one server, access a common file, make changes, observe synchronization, experience a deliberate conflict scenario, and recover from client disconnection/reconnection.
The project will be developed progressively with Git, tested throughout the development period, and demonstrated live during evaluation.

27. Team Commitment
All three members agree to:
Contribute progressively throughout the project duration.
Maintain meaningful Git commits.
Understand the code they submit.
Participate in testing.
Participate in the live demonstration.
Be able to explain the major design decisions.
Follow the declared AI-usage plan.
Avoid relying on AI-generated material that the team cannot explain.
Prepare the project before the final deadline of 11 October 2026.

Project Selected
Project 4 — Collaborative Network File System
Team Members: 3
Development Approach: Client-server system running on the same host initially
Primary Networking Concept: Multi-client client-server communication
Primary Distributed-System Concept: Concurrent access and conflict resolution
Live Demo: Three clients + one server + normal edit + conflict + disconnect/reconnect
Final Deadline: 11 October 2026
