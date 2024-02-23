#kills a running process
exec {'kill_process':
  command => 'pkill killmenow',
  onlyif => 'pgrep killmenow',
}

