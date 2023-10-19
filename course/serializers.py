from rest_framework import serializers

from course.models import Course, Lesson, Payment



class LessonSerializer(serializers.ModelSerializer): # Это сериалайзер. Этот сериалайзер описывает то что я буду видеть в Postman
    class Meta:
        model = Lesson
        fields = '__all__'
        #validators = [Validatot_url(field='name')]


class CourseSerializer(serializers.ModelSerializer):  # Описываем сериализатор
    count_lesson = serializers.SerializerMethodField()   #2 Метод подсчёта уроков
    lessons = LessonSerializer(many=True, read_only=True)  # Заданиe 3  # Кастомное поле(дополнительное)  Тоесть переменная lessons равна всем значениям LessonSerializer

    class Meta:
        model = Course
        fields = ['name', 'description', 'lessons', 'count_lesson']

    def get_count_lesson(self, instance):    #2 Метод подсчёта уроков
        return instance.lessons.all().count()


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


# class SubscriptionSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Subscription
#         fields = ('course', 'user')
