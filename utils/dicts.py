def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.

    Примеры работы:

    >>> data = {"vcs": "mercurial"}
    >>> get_val(data, "vcs")
    'mercurial'
    >>> get_val(data, "vcs", "git")
    'mercurial'
    >>> data = {}
    >>> get_val({}, "vcs", "git")
    'git'
    >>> get_val({}, "vcs", "bazaar")
    'bazaar'
    """
    data = collection

    i = 0
    for item in data.keys():
        if item == key:
            return data[item]
        i = i + 1

    if i == len(data):
        return default