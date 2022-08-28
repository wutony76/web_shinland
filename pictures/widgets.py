from django.conf import settings
from django import forms
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class PictureSetWidget(forms.HiddenInput):

	def __init__(self, can_remove=True, *args, **kwargs):
		super(PictureSetWidget, self).__init__(*args, **kwargs)
		self.can_remove = can_remove

	def render(self, name, value, attrs=None):
		_input = super(PictureSetWidget, self).render(name, value, attrs)

		output = []

		widget_id = "%s-widget" % name
		link_id = "%s-setlink" % name

		if value:
			output.append('<div class="widget-picture"><img src="%s?w=256&h=256"></div>' % reverse('pictures:picture', args=[value]))
		else:
			output.append('<div class="widget-picture"></div>')	

		output.append(u'<a id="%s" href="%s?widget=%s">選擇圖片</a><br/>' % (
			link_id,
			reverse('pictures:picture_set'),
			widget_id,
			)
		)
		if self.can_remove:
			if value:
				output.append(u'<a class="remove" href="javascript:void(0)">移除圖片</a>')
			else:
				output.append(u'<a class="remove" style="display: none;" href="javascript:void(0)">移除封面圖片</a>')



		output.append(u"""<script type="text/javascript">
				$("#%(link_id)s").facebox();
				$("#%(widget_id)s .remove").click(function(){
					$("#id_%(input_id)s").val('');
					$("#%(widget_id)s .widget-picture").html('');
					$(this).hide();
					return false;
				});
				</script>""" % {
					'widget_id':	widget_id,
					'input_id': name,
					'link_id': link_id,
				}

		)

		resulet = '<div id="%s">%s%s</div>' % (widget_id, _input, u''.join(output))

		return mark_safe(resulet)

	class Media:
		css = {
				'all': ('facebox/facebox.css',)
				}
		js = ('js/jquery-1.6.2.js', 'facebox/facebox.js')

class WysiwygWidget(forms.Textarea):

	def render(self, name, value, attrs=None):
		defaults = {
				'cols': 120,
				'rows': 30,
				}
		defaults.update(attrs or {})
		textarea = super(WysiwygWidget, self).render(name, value, defaults)
		result = u"""
		<br class="clear" />
		<div id="%(container_id)s">
		%(textarea)s
		</div>
		<a id="%(html_mode_id)s" href="">html編輯模式</a>
		<a id="%(editor_mode_id)s" style="display: none;" href="">編輯器模式</a>
		<script type="text/javascript">

			function change_editor() {
				$($("#%(textarea_id)s")).wysiwyg({insert_image_url: "%(insert_url)s"});
				$(".wysiwyg").prev().addClass('wysiwyg-label').addClass('clearfix');
				$("#%(textarea_id)sIFrame").load(function(){
					$(this).contents().find('img').dblclick(function(){
						var img = $(this);
						$($.facebox).bind('reveal.facebox', function(){							
							$("#facebox #image-info-url").val($(img).attr('src'));
							$("#facebox #image-info-url").focus();
							$("#facebox form").bind('submit', function(){
								$(img).attr('src', $("#facebox #image-info-url").val());
								$.facebox.close();
								return false;
							});
						});

						$.facebox({ajax: '%(STATIC_URL)sjwysiwyg/image_info.html'});						
						
					});
				});
			}

			$(function(){
				change_editor();			

				$("#%(html_mode_id)s").click(function(){
					var input = $('<textarea id="%(textarea_id)s" name="%(name)s" rows="30" cols="120"></textarea>');
					$(input).html($("#%(textarea_id)s").wysiwyg('getContent').html());
					
					$("#%(container_id)s").html('');
					$("#%(container_id)s").append(input);
					$(this).hide();
					$("#%(editor_mode_id)s").show();
					return false;
				});

				$("#%(editor_mode_id)s").click(function(){
					change_editor();			

					$(this).hide();
					$("#%(html_mode_id)s").show();
					return false;
				});


			});
		</script>
		"""
		result = result % {
				'textarea': textarea,
				'name': name,
				'textarea_id': 'id_%s' % name,
				'insert_url': reverse('pictures:insert'),
				'html_mode_id': 'id_%s_html_mode' % name,
				'editor_mode_id': 'id_%s_editor_mode' % name,
				'container_id': 'id_%s_container' % name,
				'STATIC_URL': settings.STATIC_URL
				}
		return mark_safe(result)


	class Media:
		css = {
				'all': ('jwysiwyg/jquery.wysiwyg.css', 'jwysiwyg/wysiwyg.custom.css', 'facebox/facebox.css')
				}
		js = ('js/jquery-1.6.2.js', 'jwysiwyg/jquery.wysiwyg.js', 'facebox/facebox.js')
