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

    def parse_window_name(self, text):
        text = ""
        return text

    def minimize_all(self, qtile):
        """Минимизирует/восстанавливает все окна в текущей группе."""
        # Получаем текущую активную группу
        current_group = qtile.current_group

        # Перебираем все окна в этой группе
        for window in current_group.windows:
            # Вызываем команду переключения минимизации для каждого окна
            if hasattr(window, "toggle_minimize"):
                window.toggle_minimize()

    def kill_all(self, qtile):
        """Закрывает все окна в текущей группе."""
        # Получаем текущую активную группу
        current_group = qtile.current_group

        # Создаем список окон для безопасного удаления,
        # так как итератор может быть нарушен при закрытии
        windows_to_kill = list(current_group.windows)

        # Перебираем окна и закрываем каждое
        for window in windows_to_kill:
            # Для закрытия окна используется команда .kill()
            window.kill()


commands = Commands()
