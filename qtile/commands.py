from subprocess import check_output


class Commands:

    def get_keyboard(self):
        display_map = {
            "us": "🇺🇸 ",
            "ru": "🇷🇺 ",
        }
        keyboard = (
            check_output("xkb-switch -p",
                         shell=True).decode("utf-8").replace("\n", "")
        )

        return display_map[keyboard]


commands = Commands()
