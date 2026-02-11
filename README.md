# ralph-wiggum-fun-app

This repo demonstrates a sample flow how to generate an application with IBM Bob and the Ralph Wiggum loop. Check the git history for how it evolved.

For a description read the blog post: [Bob meets Ralph](https://heidloff.net/article/bob-ralph-wiggum/)

[IBM Bob](https://www.ibm.com/products/bob) is an AI SDLC (Software Development Lifecycle) partner that helps developers work confidently with real codebases. Bob augments your existing workflows and provides proactive insights. It supports developers as they reason about code and make decisions.


## Step 1 - Product Requirements Document

First a Product Requirement Document is created. This is done via the Bob IDE.

```
Create a high quality Product Requirements Document (PRD) to build software. If there is information missing, let's discuss and ask me questions until you have all necessary information. 

The following information must NOT be put in the PRD:
- Multiple options how to implement features
- Potential future improvements
- Necessary approvals

Build an application with two funny samples about Ralph Wiggum from the Simpsons.
```

Bob asks some questions and gives options. The user selects:

* A simple command-line tool or script
* Python (easy to run, good for CLI tools)
* Display random Ralph Wiggum quotes when run

Before the PRD is created the user adds the following instruction:

```
Add another example to help Ralph with his homework. Ralph is not very good at math, but he tries his best. If the sum is greater than 10, it is "too hard" for Ralph.
```

The output of this step is the [PRD](application/ralph/PRD_Ralph_Wiggum_App.md).