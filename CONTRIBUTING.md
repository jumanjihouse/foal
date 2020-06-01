# Contributing

<!--TOC-->

- [GitHub flow](#github-flow)
- [Helper scripts](#helper-scripts)
  - [Bootstrap your DevEnv](#bootstrap-your-devenv)
  - [Build and test](#build-and-test)
- [Commit message](#commit-message)
- [More details on commits](#more-details-on-commits)

<!--TOC-->

## GitHub flow

Please follow [Github flow](https://guides.github.com/introduction/flow/index.html).

This is a rough outline of the workflow:

- Create a topic branch from where you want to base your work. This is usually master.
- Make commits of logical units (and add tests!).
- Make sure your commit messages are in the proper format (see below).
- Push your changes to a topic branch in your fork of the repository.
- Submit a pull request.
- Rebase and force-push to your fork's branch as necessary.

Thanks for you contributions!


## Helper scripts

### Bootstrap your DevEnv

```bash
sdlc/bootstrap
```


### Build and test

```bash
sdlc/build
sdlc/test
```


## Commit message

This is an example of a commit message:

```conf
add a cluster test command

this uses tmux to setup a test cluster that you can easily kill and
start for debugging.
```

The subject line fills in the blank of the sentence:

```conf
When this commit is merged, it will __________________________ .
```

This allows the message to be easier to read on github
as well as in various git tools.

- The **subject** line contains succinct description of the change.
  - use imperative mood, present tense
  - no dot (.) at the end
  - max 72 chars

- The **body** describes *why* the change is necessary.
  - use imperative mood, present tense
  - include motivation for the change and contrasts with previous behavior
  - wrap lines at 72 chars when possible for text
  - wrap lines at 100 chars when possible for code blocks


## More details on commits

- https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
- https://chris.beams.io/posts/git-commit/
- https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits
