import kotlinx.serialization.Serializable
import kotlinx.serialization.SerialName

@Serializable
data class Incident(
    val id: Long? = null,
    val description: String,
    val latitude: Double,
    val longitude: Double,
    val severity: String = "unknown",
    @SerialName("reporter_id")
    val reporterId: String? = null,
    @SerialName("created_at")
    val createdAt: String? = null,
)
