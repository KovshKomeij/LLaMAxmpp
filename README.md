# LLaMAxmpp
Чат бот LLaMA для XMPP на языке программиярования python<br><br>
<img src="screenshot1.png"><br>
Демонстрация работы LLaMAxmpp на основе языковой модели TinyLLaMA<br>
# Установка LLaMAxmpp:
Для установки LLaMAxmpp потребуется:
<ol>
  <li>Установить для python пакеты: <code>slixmpp llama-cpp-python translate langdetect</code> (Работает только на Линуксе)</li>
  <li>Скачать с https://huggingface.co или с другого источника, языковую модель LLaMA или другую с расширением .gguf, .ggml или .bin, и поместить её в любое удобное место</li>
  <li>Склонировать репозиторий: <code>git clone https://github.com/KovshKomeij/LLaMAxmpp.git</code></li>
  <li>Поднастроить файл <code>main.py</code> и поменять тут: расположение к языковой модели, максимальное колличество токенов, описание бота и логин с паролем в XMPP</li>
  <li>Запустить бот с помощью команды <code>python3 main.py</code> или <code>python main.py</code>, если не вылетело никаких ошибок то вы можете использовать бота!</li>
</ol>
