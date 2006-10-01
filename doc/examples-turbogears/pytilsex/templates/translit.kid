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

<h2>pytils.translit</h2>

<h3>pytils.translit.translify</h3>
<p>Простая транслитерация, из текста <blockquote>${text}</blockquote> 
получается <blockquote><em>${pytils.translit.translify(text)}</em></blockquote>
</p>

<p>В шаблоне записано так:
<code><pre>
&lt;p&gt;Простая транслитерация, из текста &lt;blockquote&gt;$${text}&lt;/blockquote&gt; 
получается &lt;blockquote&gt;&lt;em&gt;$${pytils.translit.translify(text)}&lt;/em&gt;&lt;/blockquote&gt;
&lt;/p&gt;
</pre></code>
</p>

<h3>pytils.translit.detranslify</h3>
<p>Простая детранслитерация, из текста <blockquote>${translit}</blockquote> 
получается <blockquote><em>${pytils.translit.detranslify(translit)}</em></blockquote>
</p>

<p>В шаблоне записано так:
<code><pre>
&lt;p&gt;Простая детранслитерация, из текста &lt;blockquote&gt;$${translit}&lt;/blockquote&gt; 
получается &lt;blockquote&gt;&lt;em&gt;$${pytils.translit.detranslify(translit)}&lt;/em&gt;&lt;/blockquote&gt;
&lt;/p&gt;
</pre></code>
</p>

<h3>pytils.translit.slugify</h3>
<p>Подготовка текста для URL. Из текста <blockquote>${text}</blockquote> 
получается slug <blockquote><em>${pytils.translit.slugify(text)}</em></blockquote>
Также возможна обработка и английского текста: например из 
<blockquote>${translit}</blockquote> получается slug 
<blockquote><em>${pytils.translit.slugify(translit)}</em></blockquote></p>

<p>В шаблоне это всё записано так:
<code><pre>
&lt;p&gt;Подготовка текста для URL. Из текста &lt;blockquote&gt;$${text}&lt;/blockquote&gt; 
получается slug &lt;blockquote&gt;&lt;em&gt;$${pytils.translit.slugify(text)}&lt;/em&gt;&lt;/blockquote&gt;
Также возможна обработка и английского текста: например из 
&lt;blockquote&gt;$${translit}&lt;/blockquote&gt; получается slug 
&lt;blockquote&gt;&lt;em&gt;$${pytils.translit.slugify(translit)}&lt;/em&gt;&lt;/blockquote&gt;&lt;/p&gt;
</pre></code></p>


</div>
</body>
</html>
