import json
import os

def vscode_workspace(envdir):
	main_folders = ['code', 'config', 'data', 'notes', 'work']

	setup = {
		"folders": [],
		"settings": {
			"workbench.colorTheme": "Night Owl (No Italics)",
			"workbench.iconTheme": "vscode-icons",
			"editor.rulers": [79]
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
				"tomoki1207.pdf"
			]
		},
	}

	# Add the environment_setup folder
	if os.getcwd().split(os.sep)[-1] == 'environment_setup':
		setup['folders'].append({"path": os.getcwd()})
	elif os.path.exists(os.path.join(os.getcwd(), 'environment_setup')):
		structure = os.path.join(os.getcwd(), 'environment_setup')
		setup['folders'].append({"path": structure})
	else:
		print("Unable to find environment_setup directory. Not added to workspace.")
	

	# Add all of the Environment folders
	for folder in main_folders:
		add_folder = {
			"path": os.path.join(envdir, folder)
		}
		setup['folders'].append(add_folder)

	# Add the hidden and backup folders
	setup['folders'].append({"path": os.path.join(os.path.expanduser('~'), '.aws')})
	setup['folders'].append({"path": os.path.join(os.path.expanduser('~'), '.ssh')})
	setup['folders'].append({"path": os.path.join(os.path.expanduser('~'), 'backups')})

	# Write the json config to environment.code-workspace file in config folder
	with open(os.path.join(envdir, 'config', 'environment.code-workspace'), 'w') as f:
		f.write(json.dumps(setup, indent=4))

	return

