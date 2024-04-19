# Changing OS config so one can login with holberton user
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }

