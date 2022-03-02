import { resolver } from "blitz"
import db from "db"
import { z } from "zod"

const UpdateQuestion = z.object({
  id: z.number(),
  text: z.string(),
})

export default resolver.pipe(
  resolver.zod(UpdateQuestion),
  resolver.authorize(),
  async ({ id, ...data }) => {
    // TODO: in multi-tenant app, you must add validation to ensure correct tenant
    const question = await db.question.update({ where: { id }, data })

    return question
  }
)
