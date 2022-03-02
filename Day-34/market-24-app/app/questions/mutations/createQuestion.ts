import { resolver } from "blitz"
import db from "db"
import { z } from "zod"

const CreateQuestion = z.object({
  text: z.string(),
})

export default resolver.pipe(resolver.zod(CreateQuestion), resolver.authorize(), async (input) => {
  // TODO: in multi-tenant app, you must add validation to ensure correct tenant
  const question = await db.question.create({ data: input })

  return question
})
