# Using Puppet, create a file in /tmp.
File_path { '/tmp/holberton':
  permission => '0744',
  owner      => 'www-data',
  group      => 'www-data',
  contains   => 'I love Puppet',
}
