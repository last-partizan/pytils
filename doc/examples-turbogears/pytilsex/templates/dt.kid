<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<?python
import pytils
?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>PyTils Demo</title>
</head>
<body>
<div id="header">&nbsp;</div>
<div id="main_content">
	<h1><a href="/">PyTils Demo</a></h1>

<h2>pytils.dt</h2>

<h3>pytils.dt.distance_of_time_in_words</h3>
<p>Например, тест прошлого времени был <em>${pytils.dt.distance_of_time_in_words(otime)}</em>.
Если более точно, то <em>${pytils.dt.distance_of_time_in_words(otime, 2)}</em>. Нужно
еще более точно? Пожалуйста - это было <em>${pytils.dt.distance_of_time_in_words(otime, 3)}</em>.
</p>
<p>
Точно так же (т.е. для Вас абсолютно прозрачно) и с будущим временем - следующий тест
будет <em>${pytils.dt.distance_of_time_in_words(ftime)}</em>
</p>
<p>
В шаблоне это выглядит так:
<code><pre>
&lt;p&gt;Например, тест прошлого времени был &lt;em&gt;$${pytils.dt.distance_of_time_in_words(otime)}&lt;/em&gt;.
Если более точно, то &lt;em&gt;$${pytils.dt.distance_of_time_in_words(otime, 2)}&lt;/em&gt;. Нужно
еще более точно? Пожалуйста - это было &lt;em&gt;$${pytils.dt.distance_of_time_in_words(otime, 3)}&lt;/em&gt;.
&lt;/p&gt;
&lt;p&gt;
Точно так же (т.е. для Вас абсолютно прозрачно) и с будущим временем - следующий тест
будет &lt;em&gt;$${pytils.dt.distance_of_time_in_words(ftime)}&lt;/em&gt;
&lt;/p&gt;
</pre></code>
</p>

<h3>pytils.dt.ru_strftime</h3>
<p>
Тоже всё просто - используем обычный формат strftime, в котором %a, %A, %b и %B
заменены на русские. К примеру, текущая дата: <em>${pytils.dt.ru_strftime(u"%d %B %Y, %A")}</em>.
Согласитесь, выглядит не по-русски. Чтобы месяц склонялся, используйте опцию 
<code>inflected</code>: <em>${pytils.dt.ru_strftime(u"%d %B %Y, %A", inflected=True)}</em>.
Если же нужно чтобы и день склонялся, используйте опцию <code>inflected_day</code>:
текущий тест был выполнен в <em>${pytils.dt.ru_strftime(u"%A, %d %B %Y", inflected=True, inflected_day=True)}</em>.</p>

<p>Не забудьте, что формат нужно передавать в unicode, а не в строке (как в обычном strftime).</p>

<p>Приведенный выше текст в шаблоне записан следующим образом:
<code><pre>
&lt;p&gt;Тоже всё просто - используем обычный формат strftime, в котором %a, %A, %b и %B
заменены на русские. К примеру, текущая дата: &lt;em&gt;$${pytils.dt.ru_strftime(u"%d %B %Y, %A")}&lt;/em&gt;.
Согласитесь, выглядит не по-русски. Чтобы месяц склонялся, используйте опцию 
&lt;code&gt;inflected&lt;/code&gt;: &lt;em&gt;$${pytils.dt.ru_strftime(u"%d %B %Y, %A", inflected=True)}&lt;/em&gt;&lt;/p&gt;. 
Если же нужно чтобы и день склонялся, используйте опцию &lt;code&gt;inflected_day&lt;/code&gt;:
текущий тест был выполнен в 
&lt;em&gt;$${pytils.dt.ru_strftime(u"%A, %d %B %Y", inflected=True, inflected_day=True)}&lt;/em&gt;.&lt;/p&gt;
</pre></code>
</p>

</div>
</body>
</html>
