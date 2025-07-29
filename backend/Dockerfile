FROM eclipse-temurin:17-jdk
WORKDIR /app
COPY . .
RUN ./gradlew clean build --no-daemon
CMD ["java", "-jar", "build/libs/example-0.0.1-SNAPSHOT.jar"]
