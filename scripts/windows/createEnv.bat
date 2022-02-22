mkdir logs
mkdir conf
echo [Database]>conf/settings.ini
echo filename=comptes.db>>conf/settings.ini
type nul > conf/.env