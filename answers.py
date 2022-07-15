answers = {
	"hello": "YO MAn!",
	"how is it going": "Im Doin Fine",
	"bye": "CyA",
}
print("start dialog with these words or phrases : 'hello', 'how is it going' or 'bye':")
try:
	def get_answer(question):
		q = print(question.lower())
		return q

	question = answers.get(input())
	get_answer(question)
except Exception as ex:
	print("wrong words")