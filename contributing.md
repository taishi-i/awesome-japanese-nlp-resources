# Contributing

Your contributions are always welcome!

## Finding Resources to Add

You can discover GitHub repositories not yet listed here using the `awesome-japanese-nlp-search` Claude Code plugin:

```shell
# Install the plugin (one-time setup)
/plugin marketplace add taishi-i/awesome-japanese-nlp-resources
/plugin install awesome-japanese-nlp-search@awesome-japanese-nlp-search
/reload-plugins
```

Then use the `find-new-resources` skill to search for addition candidates:

```shell
/awesome-japanese-nlp-search:find-new-resources <topic>
```

For example:

```shell
/awesome-japanese-nlp-search:find-new-resources Japanese LLM
/awesome-japanese-nlp-search:find-new-resources 日本語固有表現認識
```

The skill searches GitHub for repositories matching the topic and filters out ones already listed, making it easy to find new resources to contribute. For full documentation, see the [plugin README](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/plugins/awesome-japanese-nlp-search/README.md).

## Guidelines

You can contribute to this repository in two ways.

### 1. Make a pull request

First, please check the [content](https://github.com/taishi-i/awesome-japanese-nlp-resources#contents) you want to add. If there is no matching content, please add it to [others](https://github.com/taishi-i/awesome-japanese-nlp-resources#Others).

* Add the link: `* [project-name](http://example.com/) - A short description ends with a period.`
    * Keep descriptions concise and **short**. You only need to add it to **[README.md](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/README.md)**. The maintainer will automatically apply it to each language.

* Add project stats to the table: Add the following table content.

|Name|downloads/week|total downloads|stars|
-|-|-|-
|project name|downloads/week in PePy|total downloads in PePy|stars in GitHub|

If the project has download information in [PePy](https://pepy.tech/), please add the download information. Also, add a github star in [Shields.io - GitHub Repo stars](https://shields.io/). This will help users find the good projects.
```
|[SudachiPy](https://github.com/WorksApplications/SudachiPy)|[![Downloads](https://pepy.tech/badge/sudachipy/week)](https://pepy.tech/project/sudachipy)|[![Downloads](https://pepy.tech/badge/sudachipy)](https://pepy.tech/project/sudachipy)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiPy?style=social)|
```

If the project doesn't have download information in [PePy](https://pepy.tech/), please create a line like this.
```
|[bertknp](https://github.com/ku-nlp/bertknp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/bertknp?style=social)|
```

Submit the [pull request](https://help.github.com/articles/using-pull-requests/)!


### 2. Open issues

If you have a favorite project, let us know by opening an issue. It can be in English or Japanese. Please refer to the following issue.
[いくつかのリソースの紹介 #1](https://github.com/taishi-i/awesome-japanese-nlp-resources/issues/1)


## Credits

These contributing guidelines are taken from
- [awesome](https://github.com/sindresorhus/awesome/blob/main/contributing.md)
- [awesome-python](https://github.com/vinta/awesome-python/blob/master/CONTRIBUTING.md)
- [awesome-nlp](https://github.com/keon/awesome-nlp/blob/master/contributing.md)
