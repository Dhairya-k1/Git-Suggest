import * as vscode from 'vscode';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('git-suggest.suggest', () => {
    const binPath = path.join(context.extensionPath, 'bin');

    // Secretly add this folder to the Terminal PATH
    // The 'prepend' method ensures your 'gs' command takes priority
    context.environmentVariableCollection.prepend('PATH', binPath + path.delimiter);

    console.log('Git Suggest: gs command injected into terminal PATH');
        if (!vscode.workspace.workspaceFolders) {
            vscode.window.showErrorMessage('Git Suggest: Please open a folder first.');
            return;
        }
        const rootPath = vscode.workspace.workspaceFolders[0].uri.fsPath;
        const scriptPath = path.join(context.extensionPath, 'python_scripts', 'main.py');
        const config = vscode.workspace.getConfiguration('gitSuggest');
        const pythonCmd = config.get<string>('pythonPath') || 'python';

        // Create or reuse terminal
        let terminal = vscode.window.terminals.find(t => t.name === 'Git Suggest');
        if (!terminal) {
            terminal = vscode.window.createTerminal({
                name: 'Git Suggest',
                cwd: rootPath
            });
        }
        terminal.show();
        terminal.sendText(`${pythonCmd} "${scriptPath}"`);
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}