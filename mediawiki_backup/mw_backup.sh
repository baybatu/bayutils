#!/bin/bash

# Backup script for MediaWiki. As default, configurations are
# for MAMP on OSX. You have to change database configurations and
# BACKUP_PATH variable value before use.

# Batuhan Bayrakçı <batuhanbayrakci@gmail.com>

# Database Configs
DATABASE_NAME='MY_DATABASENAME'
DATABASE_USERNAME='MY_MySQL_USERNAME'
DATABASE_PASSWORD='MY_MySQL_PASSWORD'

WIKI_DIR_NAME_IN_HTDOCS='wiki'

# Full path for backup
BACKUP_PATH='/Users/myuser/wiki_backup'

FNAME=`date +%Y-%m-%d`
ZIP_FNAME="wiki_backup_$FNAME.zip"

# mysqldump path
MYSQLDUMP_PATH='/Applications/MAMP/Library/bin'

# Apache
HTDOCS='/Applications/MAMP/htdocs'

cd $HTDOCS

echo "DB is backing up..."
$MYSQLDUMP_PATH/mysqldump --database $DATABASE_NAME -u $DATABASE_USERNAME -p$DATABASE_PASSWORD > $FNAME.sql 
if [ $? -ne 0 ]; then
    echo "Check yo dumping parameters before wreck yoself!"
    exit 1;
fi

echo "Wiki and SQL dump file is zipping..."
zip -r $ZIP_FNAME ./$WIKI_DIR_NAME_IN_HTDOCS $FNAME.sql

echo "Zipping is succeed."
echo "The zip file is being moved to the backup path:$BACKUP_PATH"
rm -rf $BACKUP_PATH
mkdir $BACKUP_PATH
mv $ZIP_FNAME $BACKUP_PATH
rm -rf $FNAME.sql