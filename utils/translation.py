import i18n

def i18n_loading(translationPath : str, locale : str) -> None:
    """
        Cette fonction charge les fichiers de traduction

        :param translationPath: Le dossier des fichiers de traduction
        :type translationPath: str
        :param locale: La locale a utiliser
        :type locale: str
    """    
    i18n.load_path.append(translationPath)
    i18n.set('locale', locale)
    i18n.set('fallback', 'en')