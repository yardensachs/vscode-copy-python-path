const vscode = require('vscode');
const copy_paste = require('copy-paste');
const child_process = require('child_process');

function activate(context) {
    let disposable = vscode.commands.registerCommand('extension.copyPyPath', function () {

        var pyexec = vscode.workspace.getConfiguration().python.pythonPath
        var filename = vscode.window.activeTextEditor.document.fileName;
        var py_proc = child_process.spawnSync(pyexec, [__dirname + '/get_path.py', filename]);
        var pypath = py_proc.stdout.toString();

        if(pypath){

            copy_paste.copy(pypath);
            vscode.window.showInformationMessage(pypath + ' was copied to clipboard');

        } else {
            vscode.window.showInformationMessage('Python path was not found');
        }

    });

    context.subscriptions.push(disposable);
}
exports.activate = activate;

function deactivate() {
}
exports.deactivate = deactivate;