from django.http import JsonResponse
from datetime import datetime
import pytz


def user_data(request):
	slack_name = request.GET.get('slack_name', '')
	track = request.GET.get('track', '')
	d = datetime.now()
	utc_time = datetime.now(pytz.utc)
	data = {
		'slack_name': slack_name,
		'current_day': d.strftime("%A"),
		'utc_time': utc_time,
		'track': track,
		'github_file_url': 'https://github.com/bukeme/hng-user-api/blob/master/api/views.py',
		'github_repo_url': 'https://github.com/bukeme/hng-user-api',
		'status_code': 200,
	}
	return JsonResponse(data, status=200)