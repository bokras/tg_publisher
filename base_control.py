import sqlite3
import os

class Control:


    def __init__(self):
        self.base_path = os.path.abspath("data/base.db")


    def get_joined_data_channels(self):
        try:
            result = []
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            gg

            cursor = conn.cursor()

            # Выполнение запроса для получения всех данных из таблицы joined_channels
            cursor.execute("SELECT * FROM joined_channels")
            data = cursor.fetchall()
            # Закрытие соединения с базой данных
            conn.close()
            for row in data:
                id = row[0]
                name = row[1]
                item = {"name": name, "id": id}
                result.append(item)
            return result
        except:
            return None

    def check_joined_channel_exists(self, name):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Проверяем, есть ли запись с таким именем в таблице
            cursor.execute("SELECT * FROM joined_channels WHERE name = ?", (name,))
            result = cursor.fetchone()

            return result is not None

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
            return False
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def create_joined_channel(self, name, id):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Создаем новую запись
            cursor.execute("INSERT INTO joined_channels (name, id) VALUES (?, ?)", (name, id))
            conn.commit()
            print(f"Новая запись с именем '{name}' и id '{id}' создана в таблице joined_channels.")
            return True

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
            return False
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def delete_joined_channel(self, name):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Проверяем, есть ли запись с таким именем в таблице
            cursor.execute("SELECT * FROM joined_channels WHERE name = ?", (name,))
            result = cursor.fetchone()

            if result is not None:
                # Если запись существует, удаляем ее
                cursor.execute("DELETE FROM joined_channels WHERE name = ?", (name,))
                conn.commit()
                print(f"Запись с именем '{name}' удалена из таблицы joined_channels.")
            else:
                print(f"Запись с именем '{name}' не найдена в таблице joined_channels.")

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def check_used_post_exists(self, post_id):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Проверяем, есть ли запись с таким id в таблице used_posts
            cursor.execute("SELECT * FROM used_posts WHERE post_id = ?", (post_id,))
            result = cursor.fetchone()

            return result is not None

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
            return False
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def create_used_post(self, post_id):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Создаем новую запись
            cursor.execute("INSERT INTO used_posts (post_id) VALUES (?)", (post_id,))
            conn.commit()
            print(f"Новая запись с id '{post_id}' создана в таблице used_posts.")

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def delete_used_post(self, post_id):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Проверяем, есть ли запись с таким id в таблице
            cursor.execute("SELECT * FROM used_posts WHERE post_id = ?", (post_id,))
            result = cursor.fetchone()

            if result is not None:
                # Если запись существует, удаляем ее
                cursor.execute("DELETE FROM used_posts WHERE post_id = ?", (post_id,))
                conn.commit()
                print(f"Запись с id '{post_id}' удалена из таблицы used_posts.")
            else:
                print(f"Запись с id '{post_id}' не найдена в таблице used_posts.")

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрытие соединения с базой данных
            conn.close()
    def get_admins(self):
        try:
            result = []
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Выполнение запроса для получения всех данных из таблицы joined_channels
            cursor.execute("SELECT * FROM admins")
            data = cursor.fetchall()
            # Закрытие соединения с базой данных
            conn.close()
            for row in data:
                name = row[0]
                id = row[1]
                item = {"name": name, "id": id}
                result.append(item)
            return result
        except:
            return None

    def create_admin(self, id, name):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Создание новой записи в таблице admins
            cursor.execute("INSERT INTO admins (id, name) VALUES (?, ?)", (id, name))
            conn.commit()
            print(f"Новая запись с id '{id}' и именем '{name}' создана в таблице admins.")
            return True
        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
            return False
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def delete_admin(self, id):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Проверяем, есть ли запись с таким id в таблице admins
            cursor.execute("SELECT * FROM admins WHERE id = ?", (id,))
            result = cursor.fetchone()

            if result is not None:
                # Если запись существует, удаляем ее
                cursor.execute("DELETE FROM admins WHERE id = ?", (id,))
                conn.commit()
                print(f"Запись с id '{id}' удалена из таблицы admins.")
            else:
                print(f"Запись с id '{id}' не найдена в таблице admins.")

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def create_active_post(self, post_text, channel_id):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Создание новой записи в таблице active
            cursor.execute("INSERT INTO active (post_text, channel_id) VALUES (?, ?)", (post_text, channel_id))
            conn.commit()
            print(f"Новая запись с текстом '{post_text}' и channel_id '{channel_id}' создана в таблице active.")

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def delete_active_post(self, post_text):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Проверяем, есть ли запись с таким post_text в таблице active
            cursor.execute("SELECT * FROM active WHERE post_text = ?", (post_text,))
            result = cursor.fetchone()

            if result is not None:
                # Если запись существует, удаляем ее
                cursor.execute("DELETE FROM active WHERE post_text = ?", (post_text,))
                conn.commit()
                print(f"Запись с текстом '{post_text}' удалена из таблицы active.")
            else:
                print(f"Запись с текстом '{post_text}' не найдена в таблице active.")

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def set_setting(self, key, value):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Проверяем, есть ли запись с таким key в таблице settings
            cursor.execute("SELECT * FROM settings WHERE key = ?", (key,))
            result = cursor.fetchone()

            if result is not None:
                # Если запись существует, обновляем ее
                cursor.execute("UPDATE settings SET value = ? WHERE key = ?", (value, key))
                print(f"Запись с ключом '{key}' обновлена в таблице settings.")
            else:
                # Если запись не существует, создаем новую
                cursor.execute("INSERT INTO settings (key, value) VALUES (?, ?)", (key, value))
                print(f"Новая запись с ключом '{key}' создана в таблице settings.")

            conn.commit()

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
        finally:
            # Закрытие соединения с базой данных
            conn.close()

    def get_setting(self, key):
        try:
            # Подключение к базе данных SQLite
            conn = sqlite3.connect(self.base_path)
            cursor = conn.cursor()

            # Выполнение SQL-запроса для получения значения по ключу
            cursor.execute("SELECT value FROM settings WHERE key = ?", (key,))
            result = cursor.fetchone()

            if result is not None:
                # Возвращаем значение, если запись найдена
                return result[0]
            else:
                # Если запись не найдена, возвращаем None
                return None

        except sqlite3.Error as e:
            print(f"Ошибка при работе с базой данных: {e}")
            return None
        finally:
            # Закрытие соединения с базой данных
            conn.close()


if __name__ == "__main__":
    api = Control()
    data = api.set_setting("gpt_prompt","привет")
    print(data)