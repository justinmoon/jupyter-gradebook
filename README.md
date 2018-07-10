* [Open Google Cloud Console and create or select a project](https://console.developers.google.com/project)
* [Create a service account with "owner" role and download the json credentials](https://console.developers.google.com/iam-admin/serviceaccounts) as `credentials.json` in the root of this project.
* [Enable Google Drive API](https://console.developers.google.com/apis/api/drive.googleapis.com/overview?project=757468805495)
* [Enable Google Sheets API](https://console.developers.google.com/apis/library/sheets.googleapis.com)
    * FIXME: Do we really need both enabled? What's the difference?
* Go the Google Sheet that you want to work from and share it with the `client_email` found in your `credentials.json` file.
