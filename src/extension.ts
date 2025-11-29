import * as vscode from 'vscode';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    console.log('Git Suggest is active!');


    const binPath = path.join(context.extensionPath, 'bin');
    // This secretly adds your 'bin' folder to the Terminal PATH
    context.environmentVariableCollection.prepend('PATH', binPath + path.delimiter);
    

    let disposable = vscode.commands.registerCommand('git-suggest.suggest', () => {

        // 1. Check if a folder is open
        if (!vscode.workspace.workspaceFolders) {
            vscode.window.showErrorMessage('Git Suggest: Please open a folder first.');
            return;
        }
        const rootPath = vscode.workspace.workspaceFolders[0].uri.fsPath;

        // 2. Get path to script and python executable
        const scriptPath = path.join(context.extensionPath, 'python_scripts', 'main.py');
        const config = vscode.workspace.getConfiguration('gitSuggest');
        const pythonCmd = config.get<string>('pythonPath') || 'python';

        // 3. Create or Reuse Terminal
        let terminal = vscode.window.terminals.find(t => t.name === 'Git Suggest');
        if (!terminal) {
            terminal = vscode.window.createTerminal({
                name: 'Git Suggest',
                cwd: rootPath
            });
        }

        // 4. Show Terminal and Run
        terminal.show();
        terminal.sendText(`${pythonCmd} "${scriptPath}"`);
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}