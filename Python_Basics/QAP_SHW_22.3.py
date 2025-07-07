# Начальный алгоритм

def breadth_first_search_for_file(root, target_file):
    # Создаем очередь для обхода в ширину
    queue = Queue()
    queue.enqueue((root, ""))

    while not queue.is_empty():
        current_node, current_path = queue.dequeue()

        # Обновляем текущий путь, добавляя текущее имя узла
        current_path += current_node.name + "/"

        if current_node.name == target_file:
            # Если текущий узел содержит искомый файл, возвращаем текущий путь
            return current_path

        # Добавляем детей текущего узла в очередь для дальнейшего обхода
        for child in current_node.children:
            queue.enqueue((child, current_path))

    # Если файл не найден в дереве, возвращаем None
    return None

# Во-первых, вам нужно поменять саму цель алгоритма, и вместо возврата только одного пути к файлу,
# алгоритм должен возвращать список путей ко всем файлам с указанным именем.
# Во-вторых, вам необходимо изменить алгоритм поиска таким образом, чтобы он продолжал добавлять пути к
# файлам с заданным именем в список вместо возврата первого найденного пути. Это потребует модификации
# условия проверки на совпадение и добавления найденного пути к файлу в список.

# Пример работы:

root = TreeNode("C:")

root.add_child(TreeNode("Summary.docx"))

documents = TreeNode("Documents")
root.add_child(documents)
documents.add_child(TreeNode("Homework.docx"))
documents.add_child(TreeNode("Report.docx"))
documents.add_child(TreeNode("Summary.docx"))

pictures = TreeNode("Pictures")
root.add_child(pictures)
pictures.add_child(TreeNode("Summer.jpg"))
pictures.add_child(TreeNode("Winter.jpg"))
pictures.add_child(TreeNode("Summary.docx"))

file_paths = breadth_first_search_for_files(root, 'Summary.docx')
for file_path in file_paths:
    print(file_path[:-1])
# C:/Summary.docx
# C:/Documents/Summary.docx
# C:/Pictures/Summary.docx

# Решение:

def breadth_first_search_for_files(root, target_file):
    # Создаем очередь для обхода в ширину
    queue = Queue()
    queue.enqueue((root, ""))

    paths = []  # Список для хранения путей к файлам

    while not queue.is_empty():
        current_node, current_path = queue.dequeue()

        # Обновляем текущий путь, добавляя текущее имя узла
        current_path += current_node.name + "/"

        if current_node.name == target_file:
            # Если текущий узел содержит искомый файл, добавляем путь в список путей
            paths.append(current_path)

        # Добавляем детей текущего узла в очередь для дальнейшего обхода
        for child in current_node.children:
            queue.enqueue((child, current_path))

    return paths if paths else None