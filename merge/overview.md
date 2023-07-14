# Overview

Trunk Merge is a service that enables your repository to adhere to The “Not Rocket Science Rule Of Software Engineering”: **Automatically maintain a repository of code that always passes all the tests.**

## How It Works

Trunk Merge adds an additional test pass before merging pull requests. For example, a typical developer workflow for authoring a feature and merging the code to a repository might look like this:

1. Create a feature branch from the main branch
2. Author a Change
3. Open a Pull Request
4. Tests are Run
5. Code Review
6. When tests & code review pass, Author merges request

In a repository with many contributors, the state of the main branch will have advanced significantly after step 1. Because of this, the results of the tests run in step 4 are out of date. Merge solves for this by adding another test pass to ensure no broken code lands on your main branch. A developer workflow with Merge integrated might look like this:

1. Create a feature branch from the main branch
2. Author a Change
3. Open a Pull Request
4. Tests are Run
5. Code Review
6. When tests & code review pass, Author submits pull request to Merge
7. Tests are run on a branch consisting of head of main + the pull request changes
8. If the tests pass, the pull request is merged automatically

## Demo

Watch this 5 minute demo to see how it works in practice \[block:embed] { "html": "\<iframe class="embedly-embed" src="//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2F0iC\_fK6arXI%3Fstart%3D399%26feature%3Doembed%26start%3D399\&display\_name=YouTube\&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D0iC\_fK6arXI\&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2F0iC\_fK6arXI%2Fhqdefault.jpg\&key=f2aa6fc3595946d0afc3d76cbbd25dc3\&type=text%2Fhtml\&schema=youtube" width="854" height="480" scrolling="no" title="YouTube embed" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="true">", "url": "https://www.youtube.com/watch?v=0iC\_fK6arXI", "title": "How any dev team can build like Google", "favicon": "https://www.google.com/favicon.ico", "image": "https://i.ytimg.com/vi/0iC\_fK6arXI/hqdefault.jpg" } \[/block]
