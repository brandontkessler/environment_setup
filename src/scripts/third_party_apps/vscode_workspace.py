import json
import os

def vscode_workspace(config):
	wspace = config.get('BASE', 'wspace')
	main_folders = ['code', 'configs', 'data', 'notes', 'work']

	setup = {
		"folders": [],
		"settings": {
			"workbench.colorTheme": "Night Owl (No Italics)",
			"workbench.iconTheme": "vscode-icons",
			"editor.rulers": [72, 79]
		},
		"extensions": {
			"recommendations": [
				"ms-python.vscode-pylance",
				"ms-python.python",
				"yzhang.markdown-all-in-one",
				"sdras.night-owl",
				"vscode-icons-team.vscode-icons",
				"kisstkondoros.vscode-gutter-preview",
				"equinusocio.vsc-material-theme-icons",
            	"coenraads.bracket-pair-colorizer",
				"shd101wyy.markdown-preview-enhanced",
				"tomoki1207.pdf",
				"meowteam.vscode-math-to-image"
			]
		},
	}

	# Add the workspace folder
	if os.getcwd().split(os.sep)[-1] == 'workspace':
		setup['folders'].append({"path": os.getcwd()})
	elif os.path.exists(os.path.join(os.getcwd(), 'workspace')):
		structure = os.path.join(os.getcwd(), 'workspace')
		setup['folders'].append({"path": structure})
	else:
		print("Unable to find workspace directory. Not added to workspace.")
	

	# Add all of the Workspace folders
	for folder in main_folders:
		add_folder = {
			"path": os.path.join(wspace, folder)
		}
		setup['folders'].append(add_folder)

	# Add the hidden and backup folders
	setup['folders'].append({"path": os.path.join(os.path.expanduser('~'), '.aws')})
	setup['folders'].append({"path": os.path.join(os.path.expanduser('~'), '.ssh')})
	setup['folders'].append({"path": os.path.join(os.path.expanduser('~'), 'backups')})

	# Write the json config to workspace.code-workspace file in config folder
	with open(os.path.join(wspace, 'configs', 'workspace.code-workspace'), 'w') as f:
		f.write(json.dumps(setup, indent=4))

	return

