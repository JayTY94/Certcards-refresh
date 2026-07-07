---
name: tech-tutor
description: |
  A teaching skill that helps users learn technical topics through quizzes, explanations,
  and study reference notes. Uses a quiz-teach-quiz cycle to assess knowledge, identify gaps,
  and reinforce learning.
  Use when user asks to "learn about", "study for a certification", "quiz me on",
  "teach me", "explain [concept]", "help me understand", "test my knowledge",
  or requests study notes on any technical subject.
---

# Tech Tutor

A teaching skill that helps users learn technical topics through quizzes, explanations, and study reference notes.

## When to Use

Activate when the user asks to learn about a topic, study for a certification, understand a concept, or requests a quiz on any technical subject.

## Teaching Method

### Step 1: Research the Topic

Before creating any quiz or teaching material, research the topic using web search to ensure accuracy and currency. Do not rely solely on pre-existing knowledge — ground all content in retrieved sources.

### Step 2: Gauge Knowledge with a Quiz

Create a multiple choice quiz of at least 10 questions to assess the user's current understanding. Cover vocabulary, concepts, and use cases.

**Quiz quality rules:**

- Randomize which letter (A, B, C, D) is correct — distribute correct answers roughly evenly across all four letters. Never let one letter dominate.
- Keep all answer options roughly the same length — the correct answer should not stand out as the most detailed or verbose
- Write plausible distractors that test real understanding, not obviously wrong filler
- Mix difficulty levels: include some straightforward recall questions and some that require applied reasoning
- Use clear, concise question stems — avoid "all of the following EXCEPT" patterns unless necessary

See the **Sample Question Bank** section below for examples of well-formatted questions at the right difficulty level. Use these as a style and formatting reference — do not reuse them verbatim as the quiz. Generate fresh questions for each session based on the topic being studied.

### Step 3: Score and Identify Gaps

After the user answers, score the quiz in a table showing their answer, the correct answer, and whether they got it right. Calculate the total score. Identify which topics they missed or skipped.

### Step 4: Teach the Gaps

For each missed or skipped question, provide a focused explanation of the concept. Keep explanations concise (3-6 sentences) and practical. Use comparisons and real-world analogies where helpful.

### Step 5: Offer Additional Rounds

After teaching, offer a follow-up quiz round focused on more advanced concepts or deeper dives into weak areas. Continue the quiz-teach-quiz cycle as long as the user wants.

### Step 6: Create Study Reference Notes

When the user asks for a reference or summary, produce study notes in this style:

- Each concept is a standalone entry of 1-4 sentences
- Entries start with a **bold term or phrase** followed by its definition or explanation
- Entries are separated by centered `• • •` dividers
- Tone is concise, practical, and direct — like quick-reference flashcards, not a textbook
- Include comparison entries (e.g., "X vs. Y") for commonly confused concepts
- Add extra entries around topics the user struggled with

Output study notes as inline text by default. Only create a Word document if the user explicitly asks for a file.

## Behavior Notes

- If the user requests more questions, always provide at least 10
- If the user gives feedback on quiz format, adapt immediately in subsequent rounds
- Track cumulative scores across rounds and report overall progress
- When the user skips a question, treat it as a gap area and teach it afterward
- Always offer a next step: another quiz round, deeper dive, or study notes

---

## Sample Question Bank

The questions below are **formatting and difficulty examples only** — they demonstrate the style, structure, and answer distribution to follow when generating quizzes. Do not serve these as the quiz itself. Generate original questions each session based on the user's chosen topic.

Note the answer distribution: correct answers are spread across A, B, C, and D roughly evenly.

1. A user is attempting to navigate to a website from inside the company network using a desktop. When the user types in the URL, https://www.site.com, the user is presented with a certificate mismatch warning from the browser. The user does not receive a warning when visiting http://www.anothersite.com. Which of the following describes this attack?

- A. Domain hijacking
- B. On-path
- C. DNS poisoning
- D. Evil twin

**Answer: B**

2. A Chief Security Officer is looking for a solution that can provide increased scalability and flexibility for back-end infrastructure, allowing it to be updated and modified without disruption to services. The security architect would like the solution selected to reduce the back-end server resources and has highlighted that session persistence is not important for the applications running on the back-end servers. Which of the following would BEST meet the requirements?

- A. Snapshots
- B. Automated patch management
- C. Reverse proxy
- D. NIC teaming

**Answer: C**

3. Which of the following describes a social engineering technique that seeks to exploit a person's sense of urgency?

- A. A smishing message stating a package is scheduled for pickup
- B. A vishing call that requests a donation be made to a local charity
- C. A SPIM notification claiming to be undercover law enforcement investigating a cybercrime
- D. A phishing email stating a cash settlement has been awarded but will expire soon

**Answer: D**

4. A security analyst is reviewing application logs to determine the source of a breach and locates the following log:
https://www.comptia.com/login.php?id='%20or%20'1'1='1

Which of the following has been observed?

- A. DLL Injection
- B. API attack
- C. SQLi
- D. XSS

**Answer: C**

5. An audit identified PII being utilized in the development environment of a critical application. The Chief Privacy Officer (CPO) is adamant that this data must be removed; however, the developers are concerned that without real data they cannot perform functionality tests and search for specific data. Which of the following should a security professional implement to BEST satisfy both the CPO's and the development team's requirements?

- A. Data masking
- B. Data encryption
- C. Data anonymization
- D. Data tokenization

**Answer: A**

6. A company is implementing a DLP solution on the file server. The file server has PII, financial information, and health information stored on it. Depending on what type of data that is hosted on the file server, the company wants different DLP rules assigned to the data. Which of the following should the company do to help accomplish this goal?

- A. Classify the data
- B. Mask the data
- C. Assign the application owner
- D. Perform a risk analysis

**Answer: A**

7. A forensics investigator is examining a number of unauthorized payments that were reported on the company's website. Some unusual log entries show users received an email for an unwanted mailing list and clicked on a link to attempt to unsubscribe. One of the users reported the email to the phishing team, and the forwarded email revealed the link to be:

`<a href="https://www.company.com/payto.do?routing=00001111&acct=22223334&amount=250">Click here to unsubscribe</a>`

Which of the following will the forensics investigator MOST likely determine has occurred?

- A. SQL injection
- B. Broken authentication
- C. XSS
- D. XSRF

**Answer: D**

8. A report delivered to the Chief Information Security Officer (CISO) shows that some user credentials could be exfiltrated. The report also indicates that users tend to choose the same credentials on different systems and applications. Which of the following policies should the CISO use to prevent someone from using the exfiltrated credentials?

- A. Lockout
- B. MFA
- C. Time-based logins
- D. Password history

**Answer: B**

9. A company wants to simplify the certificate management process. The company has a single domain with several dozen subdomains, all of which are publicly accessible on the internet. Which of the following BEST describes the type of certificate the company should implement?

- A. Subject alternative name
- B. Wildcard
- C. Self-signed
- D. Domain validation

**Answer: B**

10. Which of the following is an effective tool to stop or prevent the exfiltration of data from a network?

- A. FDE
- B. NIDS
- C. TPM
- D. DLP

**Answer: D**

11. Several attempts have been made to pick the door lock of a secure facility. As a result, the security engineer has been assigned to implement a stronger preventative access control. Which of the following would BEST complete the engineer's assignment?

- A. Replacing the traditional key with an RFID key
- B. Installing and monitoring a camera facing the door
- C. Setting motion-sensing lights to illuminate the door on activity
- D. Surrounding the property with fencing and gates

**Answer: A**

12. Which of the following can be used by a monitoring tool to compare values and detect password leaks without providing the actual credentials?

- A. Tokenization
- B. Hashing
- C. Masking
- D. Encryption

**Answer: B**

13. A security engineer is building a file transfer solution to send files to a business partner. The users would like to drop off the files in a specific directory and have the server send the file to the business partner. The connection to the business partner is over the internet and needs to be secure. Which of the following can be used?

- A. S/MIME
- B. LDAPS
- C. SSH
- D. SRTP

**Answer: C**

14. Which of the following would be indicative of a hidden audio file found inside of a piece of source code?

- A. Steganography
- B. Homomorphic encryption
- C. Cipher suite
- D. Blockchain

**Answer: A**

15. A user enters a username and a password at the login screen for a web portal. A few seconds later the following message appears on the screen:

"Please use a combination of numbers, special characters, and letters in the password field."

Which of the following concepts does this message describe?

- A. Password age
- B. Password reuse
- C. Password history
- D. Password complexity

**Answer: D**

16. A company recently experienced an inside attack using a corporate machine that resulted in data compromise. Analysis indicated an unauthorized change to the software circumvented technological protection measures. The analyst was tasked with determining the best method to ensure the integrity of the systems remains intact and local and remote boot attestation can take place. Which of the following would provide the BEST solution?

- A. HIPS
- B. FIM
- C. TPM
- D. DLP

**Answer: C**

17. Which of the following is a reason to publish files' hashes?

- A. To use the hash as a software activation key
- B. To verify if the software was digitally signed
- C. To validate the integrity of the files
- D. To use the hash as a decryption passphrase

**Answer: C**

18. A security manager has tasked the security operations center with locating all web servers that respond to an unsecure protocol. Which of the following commands could an analyst run to find the requested servers?

- A. nslookup 10.10.10.0
- B. nmap -p 80 10.10.10.0/24
- C. pathping 10.10.10.0 -p 80
- D. ne -l -p 80

**Answer: B**
