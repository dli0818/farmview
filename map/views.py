from django.shortcuts import render
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import simplejson as json
from .models import Config
from .models import Datafield

def map(request):
  configObj = Config.objects.order_by('-pub_date')[0]
  vizjson = urllib2.urlopen(configObj.vizjson_url).read()
  config = {
    'vizjson_url': configObj.vizjson_url,
    'vizjson': vizjson,
    'pub_date': str(configObj.pub_date),
    'optional_note': configObj.optional_note
  }
  datafield_data = list(Datafield.objects.all())
  datafields = []
  for query_field in datafield_data:
    if not query_field.enabled:
      continue
    datafield_id = str(query_field.datafield_id)
    datafield_type = str(query_field.datafield_type)
    datafield_name = str(query_field.datafield_name).strip()
    datafield_label_eng = str(query_field.datafield_label_eng)
    # datafield_label_esp = unicode(query_field.datafield_label_esp)
    data_sources = str(query_field.data_sources).replace('\r', '').split('\n')#str(query_field.data_sources).replace('\n', ',').replace('\r', '')
    query_choices_vals = str(query_field.query_choices_vals).split('\n')#.replace('\n', ',').replace('\r', '') # name in XLS Form
    query_choices_labels_eng = str(query_field.query_choices_labels_eng).split('\n')#.replace('\n', ',').replace('\r', '') # label_english in XLS Form
    # query_choices_labels_esp = unicode(query_field.query_choices_labels_esp).split('\n')#.replace('\n', ',').replace('\r', '') # label_espanol in XLS Form
    query_choices = []
    if len(query_choices_vals) == len(query_choices_labels_eng):
      for i in range(len(query_choices_vals)):
        choice_obj = {
          'val': query_choices_vals[i].strip().replace('\r', ''),
          'label_eng': query_choices_labels_eng[i].replace('\r', '')
        }
        # if len(query_choices_labels_esp) >= i + 1:
        #   choice_obj['label_esp'] = query_choices_labels_esp[i]
        query_choices.append(choice_obj)
    use_for_query_ui = query_field.use_for_query_ui
    use_for_detail_popup = query_field.use_for_detail_popup
    datafield_obj = {
      'id': datafield_id,
      'type': datafield_type,
      'name': datafield_name,
      'label_eng': datafield_label_eng,
      # 'label_esp': datafield_label_esp,
      # this is object type representation of data_sources for detailed page
      'data_sources': data_sources,
      # this is stringified representation of data_sources for query ui
      'data_sources_str': json.dumps(data_sources),
      # this is object type representation of choices for query ui
      'choices': query_choices,
      # this is stringified representation of choices for human readable values on detailed page
      'choices_str': json.dumps(query_choices),# separators=(',', ':'), sort_keys=True),
      'use_for_query_ui': use_for_query_ui,
      'use_for_detail_popup': use_for_detail_popup
    }
    datafields.append(datafield_obj)
  context = {
    'config_json': json.dumps(config),
    'datafields': datafields,
    'data_sources': ['central_coast_joined', 'data_point', 'data_polygon']
  }
  return render(request, 'map/map.html', context)
