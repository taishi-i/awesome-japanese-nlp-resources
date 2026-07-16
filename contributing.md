# Contributing

Your contributions are always welcome!

## Finding Resources to Add

You can discover GitHub repositories and Hugging Face models/datasets not yet listed here using the `awesome-japanese-nlp-resources` Claude Code plugin:

```shell
# Install the plugin (one-time setup)
/plugin marketplace add taishi-i/awesome-japanese-nlp-resources
/plugin install awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
/reload-plugins
```

Then use the `find-new-resources` skill to search for addition candidates:

```shell
/awesome-japanese-nlp-resources:find-new-resources <topic>
```

For example:

```shell
/awesome-japanese-nlp-resources:find-new-resources Japanese LLM
/awesome-japanese-nlp-resources:find-new-resources 日本語固有表現認識
```

The skill searches both GitHub and Hugging Face for repositories/models/datasets matching the topic and filters out ones already listed, making it easy to find new resources to contribute. For full documentation, see the [plugin README](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/plugins/awesome-japanese-nlp-resources/README.md).

## Guidelines

You can contribute to this repository in two ways.

### 1. Make a pull request

First, please check the [content](https://github.com/taishi-i/awesome-japanese-nlp-resources#contents) you want to add. If there is no matching content, please add it to [others](https://github.com/taishi-i/awesome-japanese-nlp-resources#others).

* Add the link: `* [project-name](http://example.com/) - A short description ends with a period.`
    * Keep descriptions concise and **short**. You only need to add it to **[README.md](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/README.md)**.

That's it — do not add a stats table row yourself. The maintainer's automated pipeline fills in the stats table (📥 downloads/week, 📦 downloads total, ⭐ GitHub stars, and the 🟢🟡🔴 last-commit indicator) and regenerates the translated versions (English, Japanese, Traditional Chinese, Simplified Chinese) on the next update, so a PR that only adds the bullet line is exactly what's expected.

Submit the [pull request](https://help.github.com/articles/using-pull-requests/)!


### 2. Open issues

If you have a favorite project, let us know by opening an issue. It can be in English or Japanese. Please refer to the following issue.
[いくつかのリソースの紹介 #1](https://github.com/taishi-i/awesome-japanese-nlp-resources/issues/1)


## Credits

These contributing guidelines are taken from
- [awesome](https://github.com/sindresorhus/awesome/blob/main/contributing.md)
- [awesome-python](https://github.com/vinta/awesome-python/blob/master/CONTRIBUTING.md)
- [awesome-nlp](https://github.com/keon/awesome-nlp/blob/master/contributing.md)
