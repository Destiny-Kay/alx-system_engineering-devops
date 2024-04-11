# Issue on wp-settings
exec { 'fix-apache-error':
        command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
        provider => 'shell'
}

