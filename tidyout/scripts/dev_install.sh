echo "🧹 unistalling tidyout"

"Yes" | pip uninstall tidyout

echo "🧼 removing build artifacts"

rm -rf build dist *.egg-info

echo "🛠 rebuilding and reinstalling"

pip install /Users/brucewayne/Code/openSourceContributions/tidyout

echo "✅ Done. tidyout is reinstalled locally"


 