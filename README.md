# viper

Viper is a Discord bot designed to reference answers from past conversations,
streamlining user interactions and improving the overall chat experience.

# Screenshots

![viper0](https://github.com/viper-Deploy2023/viper/blob/main/screenshots/viper0.png?raw=true)
![viper1](https://github.com/viper-Deploy2023/viper/blob/main/screenshots/viper1.png?raw=true)

# Installation

```shell
$ git clone git@github.com:viper-Deploy2023/viper.git
$ cd viper
$ pip install -r requirements.txt
```

# Usage

To use this program, you need to create a [Discord Application](https://discord.com/developers/applications).
Navigate to the Bot section, and find the token. To import the token as an environment
variable, run the following in the shell:

```shell
$ echo "export DISCORD_TOKEN='yourtoken'" >> ~/.bashrc
$ source ~/.bashrc
$ exec bash
```

Then, you can execute by running:

```shell
$ python main.py
```

# License

viper is licensed under [AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html), as
included in the [LICENSE](LICENSE) file.

- Copyright (C) 2023 Viper Deploy2023 Team
    * Andrew Diep <adiep@dons.usfca.edu>
	* Jake Polintan <ajpolintan@dons.usfca.edu>
	* Tao Tien <tltien@dons.usfca.edu>
    * Yiyu Zhou <yzhou155@dons.usfca.edu>

Please see the Git history for individual authorship information.
