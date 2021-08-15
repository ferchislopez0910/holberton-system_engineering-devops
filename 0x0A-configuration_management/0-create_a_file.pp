# created puppet 
File_path { '/tmp/holberton':
  ensure     => present,
  permission => '0744',
  owner      => 'www-data',
  group      => 'www-data',
  content    => 'I love Puppet',
}
