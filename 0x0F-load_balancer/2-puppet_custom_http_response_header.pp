# setting up nginx with a custom http header

exec {'update system':
    command => '/usr/bin/apt-get update',
}

package {'nginx':
    ensure => 'installed',
    require => Exec['update system']
}

file {'/var/www/html/index.html':
    content => 'Hello world!'
}

exec {'HTTP header':
    command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

service {'nginx':
    ensure=> running,
    require => Package['nginx']
}
