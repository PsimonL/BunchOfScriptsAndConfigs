import java.time.Duration

static void main(String[] args) {
    println "Measurement only in seconds, total time in {second, minute, hour, day} format."
    def startTime = System.currentTimeMillis()

    def timer = new Timer()
    timer.schedule(new TimerTask() {
        def count = 0

        @Override
        void run() {
            count++
            println "Current Time: ${count} s"
        }
    }, 1000, 1000)

    System.in.withReader { reader ->
        reader.readLine()
    }

    timer.cancel()

    def endTime = System.currentTimeMillis()
    def totalTime = Duration.ofMillis(endTime - startTime)

    def days = totalTime.toDaysPart()
    def hours = totalTime.toHoursPart()
    def minutes = totalTime.toMinutesPart()
    def seconds = totalTime.toSecondsPart()

    println "Total time: ${seconds} s, ${minutes} min, ${hours} h, ${days} d"
}
