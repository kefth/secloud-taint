function openFile () {

  dialog.showOpenDialog({ filters: [

   { name: 'json', extensions: ['json'] }

 ]},function (fileNames) {
    if (fileNames === undefined) return;
    var fileName = fileNames[0];
    document.getElementById("file_path").value = fileName;
    document.getElementById("file_note").innerHTML = fileName;
  });

}
