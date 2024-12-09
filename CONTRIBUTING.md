## Contributing

[fork]: /fork
[pr]: /compare
[style]: https://standardjs.com/
[code-of-conduct]: CODE_OF_CONDUCT.md

Hi there! We're thrilled that you'd like to contribute to this project. Your help is essential for keeping it great.

Please note that this project is released with a [Contributor Code of Conduct][code-of-conduct]. By participating in this project you agree to abide by its terms.

## Issues and PRs

If you have suggestions for how this project could be improved, or want to report a bug, open an issue! We'd love all and any contributions. If you have questions, too, we'd love to hear them.

We'd also love PRs. If you're thinking of a large PR, we advise opening up an issue first to talk about it, though! Look at the links below if you're not sure how to open a PR.

Work in Progress pull requests are also welcome to get feedback early on, or if there is something blocked you.

## Submitting a pull request

1. [Fork][fork] and clone the repository.
2. Create a new branch: `git checkout -b my-branch-name`.
3. Configure and install the dependencies: `poetry install`.
4. Make sure the tests pass on your machine: `make install & make tests`
5. Make your change, add tests, and make sure the tests still pass.
6. Push to your fork and [submit a pull request][pr] and complete the information in the pull request template.

## Linting requirements

using `make install & make tests` will also run the following linters:

- [Black: The uncompromising Python code formatter](https://black.readthedocs.io/en/stable/)
- [isort your imports, so you don't have to](https://pycqa.github.io/isort/)
- [flake8: Your Tool For Style Guide Enforcement](https://flake8.pycqa.org/en/latest/)

using `make format` will run isort and black and apply any formatting suggestions from them

## Resources

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com)
