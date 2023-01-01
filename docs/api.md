## API methods

| URl                  | Command                   | Method | Input              | Out                              |
|----------------------|---------------------------|--------|--------------------|----------------------------------|
| /api/create-url      | Create short url          | POST   | {'url': str}       | {'short_url': str, 'error': int} |
| /api/check-short-url | Check is short url exists | POST   | {'short_url': str} | {'valid': bool, 'error': int}    


## API error codes

| Error code | Status           |
|------------|------------------|
| 100        | OK               |
| 200        | Method not found |
| 300        | JSON temp error  |
| 400        | URL not found    |
| 500        | Server error     |