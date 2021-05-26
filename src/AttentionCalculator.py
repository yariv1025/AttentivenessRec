class AttentionCalc(object):
    def __init__(self, cont_weights, ratio, alpha):
        self.p_result = 0
        self.cont_weights = cont_weights
        self.ratio = ratio
        self.alpha = alpha

    def emotionValue(self, emotion):
        """
        The function receives an emotion and returns it's value.

        :param emotion: an emotion
        :return: 1 if positive emotion, else -1.
        """
        pos = ['Anticipation', 'Confidence', 'Engagement', 'Esteem', 'Excitement',
               'Happiness', 'Peace', 'Surprise']

        neg = ['Anger', 'Annoyance', 'Aversion', 'Disapproval', 'Disconnection', 'Disquietment',
               'Doubt/Confusion', 'Embarrassment', 'Fear', 'Sadness',
               'Sensitivity']

        neutral = ['Affection', 'Pleasure', 'Sympathy', 'Fatigue', 'Pain', 'Suffering', 'Yearning']

        if emotion in pos:
            return 1
        elif emotion in neg:
            return -1
        elif emotion in neutral:
            return 0
        else:
            raise ValueError("Emotion not found!")

    def emotionCalc(self, emotions):
        """
        Function for calculate the attentive levels of the subject based on emotion recognition.
        The function return value in range 0 to 10. the higher the number, the higher the level of attention.

        :param emotions: list of emotions
        :return: the subject's level of attention in scale of 0 to 10
        """
        bar = 5
        for emotion in emotions:
            bar += self.emotionValue(emotion)

        return max(0, min(10, bar))

    def contCalc(self, cont):
        valence = cont[0] * self.cont_weights[0]
        arousal = cont[1] * self.cont_weights[1]
        dominance = cont[2] * self.cont_weights[2]

        return round(valence + arousal + dominance, 2)

    def attentionCalc(self, results):
        emotion_result = self.emotionCalc(results[0])
        cont_result = self.contCalc(results[1])

        result = emotion_result * self.ratio + cont_result * (1 - self.ratio)
        self.p_result = result * self.alpha + self.p_result * (1 - self.alpha)
        print(self.p_result)
        return self.p_result
