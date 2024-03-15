{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4050cb6",
   "metadata": {
    "pycharm": {
     "is_executing": true
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [15/Mar/2024 19:04:59] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [15/Mar/2024 19:05:02] \"POST /main HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [15/Mar/2024 19:05:04] \"POST /ethical_test HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [15/Mar/2024 19:05:06] \"POST /answer HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "true\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [15/Mar/2024 19:05:08] \"POST /main HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [15/Mar/2024 19:05:09] \"POST /ethical_test HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [15/Mar/2024 19:05:10] \"POST /answer HTTP/1.1\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "false\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [15/Mar/2024 19:05:11] \"POST /end HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask,request,render_template\n",
    "app = Flask(__name__)\n",
    "\n",
    "\n",
    "@app.route(\"/\",methods=[\"GET\",\"POST\"])\n",
    "def index():\n",
    "    return(render_template(\"index.html\"))\n",
    "\n",
    "@app.route(\"/main\",methods=[\"GET\",\"POST\"])\n",
    "def main():\n",
    "    name = request.form.get(\"name\")\n",
    "    return(render_template(\"main.html\", name=name))\n",
    "\n",
    "@app.route(\"/ethical_test\",methods=[\"GET\",\"POST\"])\n",
    "def ethical_test():\n",
    "    return(render_template(\"ethical_test.html\"))\n",
    "\n",
    "@app.route(\"/answer\",methods=[\"GET\",\"POST\"])\n",
    "def answer():\n",
    "    ans = request.form[\"options\"]\n",
    "    print(ans)\n",
    "    if ans == \"true\":\n",
    "        return(render_template(\"wrong.html\"))\n",
    "    elif ans == \"false\":\n",
    "        return(render_template(\"correct.html\"))\n",
    "\n",
    "\n",
    "@app.route(\"/end\",methods=[\"GET\",\"POST\"])\n",
    "def end():\n",
    "    return(render_template(\"end.html\"))\n",
    "    \n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "name": "py37",
   "language": "python",
   "display_name": "py37"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}