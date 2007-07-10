<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<?python
import pytils
?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" py:replace="''"/>
<title>pytils demo</title>
</head>
<body>
<div id="header">&nbsp;</div>
<div id="main_content">
	<h1><a href="/">pytils demo</a></h1>

<h2>pytils.numeral</h2>

<h3>pytils.numeral.choose_plural и pytils.numera.get_plural</h3>
<p>Выбор нужной формы множественного числа. Классический пример с количеством 
комментариев: ${comment_number} 
<em>${pytils.numeral.choose_plural(comment_number, comment_variants)}</em>, 
а можно передавать только окончания: ${comment_number} комментари<em>${pytils.numeral.choose_plural(comment_number, u"й,я,ев")}</em>
</p>

<p>Код примера:
<code><pre>
&lt;p&gt;Выбор нужной формы множественного числа. Классический пример с количеством 
комментариев: $${comment_number} 
&lt;em&gt;$${pytils.numeral.choose_plural(comment_number, comment_variants)}&lt;/em&gt;, 
а можно передавать только окончания: $${comment_number} 
комментари&lt;em&gt;$${pytils.numeral.choose_plural(comment_number, u"й,я,ев")}&lt;/em&gt;
&lt;/p&gt;
</pre></code>
</p>

<p>Зачастую нужно показывать и число, и название объекта в правильной форме, а не только название
объекта. В этом случае следует воспользоваться фильтром <code>get_plural</code>. Пример с теми же
комментариями можно записать проще: 
<em>${pytils.numeral.get_plural(comment_number, u"комментарий,комментария,комментариев")}</em>.
<code>get_plural</code> удобен еще и тем, что можно указать вариант, когда значение равно нулю.
Например, гораздо симпатичней "без комментариев", чем "0 комментариев". В этом случае третим 
параметром передается нуль-вариант. Пример: 
<em>${pytils.numeral.get_plural(zero, u"пример,примера,примеров", u"без примеров")}</em>.</p>

<p>Сделано это так:
<code><pre>
&lt;p&gt;Зачастую нужно показывать и число, и название объекта в правильной форме, а не только название
объекта. В этом случае следует воспользоваться фильтром &lt;code&gt;get_plural&lt;/code&gt;. Пример с теми же
комментариями можно записать проще: 
&lt;em&gt;$${pytils.numeral.get_plural(comment_number, u"комментарий,комментария,комментариев")}&lt;/em&gt;.
&lt;code&gt;get_plural&lt;/code&gt; удобен еще и тем, что можно указать вариант, когда значение равно нулю.
Например, гораздо симпатичней "без комментариев", чем "0 комментариев". В этом случае третим 
параметром передается нуль-вариант. Пример: 
&lt;em&gt;$${pytils.numeral.get_plural(zero, u"пример,примера,примеров", u"без примеров")}&lt;/em&gt;.&lt;/p&gt;
</pre></code></p>

<h3>pytils.numeral.rubles</h3>
<p>Рубли словами. К примеру, ${rubles_value} р. словами будет
<em>${pytils.numeral.rubles(rubles_value)}</em>. У этой функции есть один 
дополнительный параметр <code>zero_for_kopeck</code>, определяющий, нужно ли нулевые копейки "проговаривать". 
Если нужно - то True, по умолчанию <code>rubles</code> этого не делает.
Пример: ${rubles_value2} р. словами будет <em>${pytils.numeral.rubles(rubles_value2)}</em>,
а с копейками - <em>${pytils.numeral.rubles(rubles_value2, zero_for_kopeck=True)}</em>.</p>

<p>Данный пример в шаблоне записан так:
<code><pre>
&lt;p&gt;Рубли словами. К примеру, $${rubles_value} р. словами будет
&lt;em&gt;$${pytils.numeral.rubles(rubles_value)}&lt;/em&gt;. У этой функции есть один 
дополнительный параметр &lt;code&gt;zero_for_kopeck&lt;/code&gt;, определяющий, нужно ли 
нулевые копейки "проговаривать". Если нужно - то True, по умолчанию 
&lt;code&gt;rubles&lt;/code&gt; этого не делает.
Пример: $${rubles_value2} р. словами будет &lt;em&gt;$${pytils.numeral.rubles(rubles_value2)}&lt;/em&gt;,
а с копейками - &lt;em&gt;$${pytils.numeral.rubles(rubles_value2, zero_for_kopeck=True)}&lt;/em&gt;.&lt;/p&gt;
</pre></code>
</p>

<h3>pytils.numeral.in_words</h3>
<p>Число словами. Можно целые, можно дробные. Примеры: ${int_value} - 
<em>${pytils.numeral.in_words(int_value)}</em>. У целых можно менять пол 
(по умолчанию - мужской, pytils.numeral.MALE): 
<em>${pytils.numeral.in_words(int_value, gender=pytils.numeral.FEMALE)}</em> (женский),
<em>${pytils.numeral.in_words(int_value, gender=pytils.numeral.NEUTER)}</em> (средний).</p>

<p>У дробных почти то же самое, только пол женский и не меняется (т.е. параметр
передавать можно, но он не будет влиять). ${float_value} словами будет
<em>${pytils.numeral.in_words(float_value)}</em>.</p>

<p>В шаблоне этот текст выглядит следующим образом:
<code><pre>
&lt;p&gt;Число словами. Можно целые, можно дробные. Примеры: $${int_value} - 
&lt;em&gt;$${pytils.numeral.in_words(int_value)}&lt;/em&gt;. У целых можно менять пол 
(по умолчанию - мужской, pytils.numeral.MALE): 
&lt;em&gt;$${pytils.numeral.in_words(int_value, gender=pytils.numeral.FEMALE)}&lt;/em&gt; (женский),
&lt;em&gt;$${pytils.numeral.in_words(int_value, gender=pytils.numeral.NEUTER)}&lt;/em&gt; (средний).&lt;/p&gt;

&lt;p&gt;У дробных почти то же самое, только пол женский и не меняется (т.е. параметр
передавать можно, но он не будет влиять). $${float_value} словами будет
&lt;em&gt;$${pytils.numeral.in_words(float_value)}&lt;/em&gt;.&lt;/p&gt;
</pre></code>
</p>

<h3>pytils.numeral.sum_string</h3>
<p>Наиболее общая функция работы с числами. Умеет "проговаривать" числа и 
одновременно представлять название объекта в нужной форме. Например, вместо 
${comment_number} комментарий(ев) можно смело писать 
<em>${pytils.numeral.sum_string(comment_number, comment_gender, comment_variants)}</em>.
</p>

<p>В коде рализовано так:
<code><pre>
&lt;p&gt;Наиболее общая функция работы с числами. Умеет "проговаривать" числа и 
одновременно представлять название объекта в нужной форме. Например, вместо 
$${comment_number} комментарий(ев) можно смело писать 
&lt;em&gt;$${pytils.numeral.sum_string(comment_number, comment_gender, comment_variants)}&lt;/em&gt;.
&lt;/p&gt;
</pre></code>
</p>


</div>
</body>
</html>
