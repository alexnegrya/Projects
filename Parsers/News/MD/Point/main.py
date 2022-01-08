import requests
import datetime
import json


class NewsParser:
   """
      Parse society news from point.md.
   """

   start_key_str = '"cparent":{"__typename":"Topic","id":"864bac82-c489-4e4b-a66f-4e6da7f8c1d1","title":{"__typename":"MultilangString","ru":"Общество"},"url":{"__typename":"MultilangString","ru":"obschestvo"},"type":"category"},"pollId":""}],"contents":['
   end_key_str = ']},"notFound":false,"categoryUrl":"obschestvo","selectedTopic":{"__typename":"Topic","id":"864bac82-c489-4e4b-a66f-4e6da7f8c1d1","title":{"__typename":"MultilangString","ru":"Общество"}'

   # News element structure
   '''
      {
         "__typename":"Content",
         "id":"<content_id>",
         "title":{
            "__typename":"ContentTitle",
            "short":"<short_title_ru>",
            "long":"<long_title_ru>"
         },
         "url":"<news_url>",
         "description":{
            "__typename":"ContentDescription",
            "intro":"^([A-Za-z]+[А-Яа-я,.]+\d+\s+)$"
         },
         "dates":{
            "__typename":"ContentDates",
            "posted":"<news_posted_date_or_time>",
            "postedWithYear":"<DD MM_short. YYYY hh:mm>",
            "postedSeparator":"<DD MM_short YYYY>",
            "postedTs":"<number>",
            "postedH":"hh:mm",
            "postedDM":"DD MM_full",
            "dateT":"<news_posted_time>"
         },
         "counters":{
            "__typename":"Counters",
            "comment":"<number_of_comments>",
            "view":"<number_of_views>",
            "like":"<number_of_likes>"
         },
         "thumbnail":"<news_image_file_name>",
         "tags":["<tag_1>","<tag_..>","<tag_n>"],
         "cparent":{
            "__typename":"Topic",
            "id":"<topic_id>",
            "title":{
               "__typename":"MultilangString",
               "ru":"Общество"
            },
            "url":{
               "__typename":"MultilangString",
               "ru":"obschestvo"
            },
            "type":"category"
         },
         "pollId":""
      }
   '''

   class NewsData:
      def __init__(self, id: str, title: dict[str: str], url: str, intro: str, full_datetime: str, comments: int, views: int, likes: int, image: str):
         self.id = id
         self.title = title
         self.url = url
         self.intro = intro
         self.full_datetime = full_datetime
         self.comments = comments
         self.views = views
         self.likes = likes
         self.image = image

      def __setattr__(self, name, value):
         if name in ('id', 'url', 'intro'):
            if type(value) != str:
               raise TypeError(f'{name} must be a string')
            object.__setattr__(self, name, value)
         elif name in ('comments', 'views', 'likes'):
            if type(value) != int:
               raise TypeError(f'{name} must have an integer value')
            object.__setattr__(self, name, value)
         elif name == 'image':
            if type(value) != str:
               raise TypeError('image attribute must have a string value')
            else:
               spl = value.split('.')
               if len(spl) == 1:
                  raise ValueError(
                      'wrong file name in string of image attribute')
               object.__setattr__(self, name, value)
         elif name == 'title':
            if type(value) != dict:
               raise TypeError('title must be a dictionary')
            else:
               for key, v in value.items():
                  if type(key) != str and type(v) != str:
                     raise TypeError(
                         f"title dictionary key '{key}' and '{v}' must be a string")
                  elif type(key) != str:
                     raise TypeError(
                         f"title dictionary key '{key}' must be a string")
                  elif key not in ('short', 'long'):
                     raise ValueError(
                         "title dictionary must contain only short and long title (for example, \{'short': 'В центральном парке Кишинева многолюдно вечером', 'long': 'В центральном парке Кишинева многолюдно вечером, люди со всех районов Кищинева стремятся его посетить'\})")
                  elif type(v) != str:
                     raise TypeError(
                         f"title dictionary value '{v}' under key '{key}' must be a string")
               object.__setattr__(self, name, value)
         elif name == 'full_datetime':
            # This argument format
            '''
                     "<time> <day> <month> <year>"
                        V      |      |       |
               <hours:minuts>  V      |       |
             <two_digit_day_number>   V       |
                       <russian_month_name>   V
                                 <four_digit_year_number>
            '''
            if type(value) != str:
               raise TypeError(
                   'full datetime argument must have a string value')
            else:
               spl = value.split(' ')
               data = {'time': spl[0], 'day': spl[1],
                       'month': spl[2], 'year': spl[3]}
               arg = "full datetime argument"

               def get_months():
                  return (
                      'Января', 'Февраля',
                      'Марта', 'Апреля', 'Мая',
                      'Июня', 'Июля', 'Августа',
                      'Сентября', 'Октября', 'Ноября',
                      'Декабря'
                  )
               # Validators

               def validate_time(time: str):
                  child_arg = f"time in {arg}"
                  if ':' not in time:
                     raise ValueError(f"{arg} must match the pattern 'hh:mm'")
                  else:
                     t = time.split(':')
                     arg_hours = f"hours of {child_arg}"
                     arg_minuts = f"minuts of {child_arg}"
                     # Checking for numeric
                     if not t[0].isnumeric():
                        raise ValueError(f"{arg_hours} must be numeric")
                     elif not t[1].isnumeric():
                        raise ValueError(f"{arg_minuts} must be numeric")
                     # Checking hours for value
                     hours_value = int(t[0])
                     if hours_value < 0:
                        raise ValueError(f"{arg_hours} must be greater than 0")
                     elif hours_value > 23:
                        raise ValueError(f"{arg_hours} must be lesser than 24")
                     # Checking minuts for value
                     minuts_value = int(t[1])
                     if minuts_value < 0:
                        raise ValueError(
                            f"{arg_minuts} must be greater than 0")
                     elif minuts_value > 59:
                        raise ValueError(
                            f"{arg_minuts} must be lesser than 60")

               def validate_year(year: str):
                  child_arg = f"year in {arg}"
                  year = int(year)
                  if year < 1900:
                     raise ValueError(f"{child_arg} must be greater than 1900")
                  elif year > datetime.now().year:
                     raise ValueError(
                         f"{child_arg} must be lesser than current year")

               def validate_month(month: str):
                  child_arg = f"month in {arg}"
                  if month not in get_months():
                     raise ValueError(f"{child_arg} is wrong")

               def validate_day(year: str, month: str, day: str):
                  child_arg = f"day in {arg}"
                  year = int(year)
                  months = get_months()
                  day = int(day)
                  if day < 1:
                     raise ValueError(f"{child_arg} must be greater than 0")
                  message = "under this month must be greater than"
                  error = f"{child_arg} {message}"

                  def check_day(months_index=None, days=None, cycle_data=()):
                     if len(cycle_data) == 3:
                        for value in cycle_data:
                           if type(value) != int:
                              raise TypeError(
                                  'cycle range must contain only integer values')
                        # cycle_data[0] - start months_index
                        # cycle_data[1] - excluding stop months_index
                        # cycle_data[2] - start days value
                        days = cycle_data[2]
                        for months_index in range(cycle_data[0], cycle_data[1]):
                           check_day(months_index, days)
                           if days == 31:
                              days = 30
                           elif days == 30:
                              days = 31
                     elif len(cycle_data) == 0 and months_index != None and days != None:
                        if month == months[months_index]:
                           if day > days:
                              raise ValueError(f"{error} {days}")
                     else:
                        raise ValueError(
                            'must specify months index and days or cycle range')
                  # January
                  check_day(0, 31)
                  # February
                  if month == months[1]:
                     leap_year = False
                     if (year % 400 == 0) and (year % 100 == 0):
                        leap_year = True
                     elif (year % 4 == 0) and (year % 100 != 0):
                        leap_year = True
                     if leap_year:
                        if day > 29:
                           raise ValueError(f"{error} 29")
                     elif day > 28:
                        raise ValueError(f"{error} 28")
                  # March, April, May, June and July
                  check_day(cycle_data=(2, 7, 31))
                  # August
                  check_day(7, 31)
                  # September, October, November and December
                  check_day(cycle_data=(8, 12, 30))
               # Vadating full_datetime data
               validate_time(data['time'])
               validate_year(data['year'])
               validate_month(data['month'])
               validate_day(data['year'], data['month'], data['day'])
               object.__setattr__(self, name, value)
      
      def __str__(self):
         title = "--- NewsData ---"
         id_ = f"ID: {self.id}"
         title = 'Title:\n'
         for key in self.title:
            if key == 'short':
               title += f"   Short: {self.title[key]}\n"
            elif key == 'long':
               title += f"   Long: {self.title[key]}"
         url = f"URL: {self.url}"
         intro = f"Intro: {self.intro}"
         full_datetime = f"Posted time and date: {self.full_datetime}"
         comments = f"Number of comments: {self.comments}"
         views = f"Number of views: {self.views}"
         likes = f"Number of likes: {self.likes}"
         image = f"Image file name: {self.image}"
         return f"{title}\n{id_}\n{title}\n{url}\n{intro}\n{full_datetime}\n{comments}\n{views}\n{likes}\n{image}"

      def __repr__(self):
         return f"<NewsData {self.id}: {self.title['short']}>"

   def __init__(self, url='https://point.md/ru/novosti/obschestvo'):
      self.url = url

   def get_news(self, mode='objects'):
      """
         Send request and returns news data in a mode-defined format.
         Supported modes:
            objects - returns the list of news data objects;
            data - returns the news data in the dictionary.
      """
      supported_modes = ('objects', 'data')
      response_text = requests.get(self.url).text
      # Cheking arguments
      if type(mode) != str:
         raise TypeError('mode must be a string')
      if mode not in supported_modes:
         modes = ', '.join([f'"{m}"' for m in supported_modes])
         raise ValueError(f'unknown mode was specified, supported modes is {modes}')
      # Getting news data string
      start_index = response_text.find(self.start_key_str)
      content_index = start_index + len(self.start_key_str)
      news_data = response_text[content_index:]
      end_index = news_data.find(self.end_key_str)
      news_data = '{' + news_data[:end_index] + '}'
      # Getting news strings
      news = []
      brackets = 0
      element = ''
      n = 0
      for char in ('{' + news_data.strip('{}') + '}'):
         element += char
         if char == '}' and brackets < 7:
            brackets += 1
         elif char == '}' and brackets == 7:
            brackets = 0
            n += 1
            element = f'"NewsData {n}":' + element.lstrip(',')
            news.append(element)
            element = ''
      data = json.loads('{' + ', '.join(news) + '}')
      if mode == 'data':
         return data
      elif mode == 'objects':
         objects = []
         for key in data:
            elem = news_data[key]
            obj = self.NewsData(
               elem['id'],
               {
                  'short': elem['title']['short'],
                  'long': elem['title']['long']
               },
               elem['url'],
               elem['description']['intro'],
               f"{elem['dates']['postedH']} {elem['dates']['postedDM']} {elem['dates']['postedSeparator'][-4:]}",
               elem['counters']['comment'],
               elem['counters']['view'],
               elem['counters']['like'],
               elem['thumbnail']
            )
            objects.append(obj)
         return objects


# Getting and print objects for demonstration
if __name__ == '__main__':
   parser = NewsParser()
   news = parser.get_news()
   for n in news:
      print(n)
