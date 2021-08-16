# using Puppet to make changes to our configuration file
# usa un metodo file line que escribe una linea en un archivo
file_line { 'param_key_default':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
# se inactiva la autenticacion normal
file_line { 'Turn_off_passwd_auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
