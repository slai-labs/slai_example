var initialize = function () {
  console.log('initializing...')
  $('#header').toggle()
  $('div#site').toggleClass('noheader')
  return false
}

$('head').append(
  '<style type="text/css"> .noheader { height: 100% !important }</style>',
)

Jupyter.notebook.config.loaded.then(initialize)
