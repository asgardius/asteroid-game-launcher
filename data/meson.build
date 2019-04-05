configure_file(
  input: 'com.example.first_application.desktop',
  output: 'com.example.first_application.desktop',
  copy: true,
  install: true,
  install_dir: join_paths(get_option('datadir'), 'applications')
)

install_data('com.example.first_application.svg',
  install_dir: join_paths(get_option('datadir'), 'icons', 'hicolor', 'scalable', 'apps'))
